from dataclasses import dataclass
import json
from optparse import Values
import requests
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.providers.postgres.hooks.postgres import PostgresHook

dag_params = {
    'dag_id' : 'weather_forecast',
    'start_date' : datetime(2022,3,11),
    'schedule_interval' : '@daily',   #once for test
    'catchup' : True, #false for test
    'params' : {
        'retries' : 2,
        'retry_delay' : timedelta(seconds=2)
    },
    'tags' : ['programmers'],
    'default_args' : {'owner':'Gyeong-Hyeon'}
}


DB_HOOK = PostgresHook(postgres_conn_id='redshift_dev_db')
API_KEY = Variable.get('openweather_key')

def get_geo_info():
    geo_info = requests.\
                get(f'http://api.openweathermap.org/geo/1.0/direct?q=seoul&limit=1&appid={API_KEY}').\
                json()
    return geo_info[0]['lat'], geo_info[0]['lon']

def get_weather(lat,lon):
    weather = requests.\
                get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric').\
                json()
    return weather

def insert_forecast_to_temp(weather):
    conn = DB_HOOK.get_conn()
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXIST kyunghyun7843.temp_weather_forecast")
    cur.execute("CREATE TABLE kyunghyun7843.temp_weather_forecast AS TABLE kyunghyun7843.weather_forecast")
    
    for day in weather['daily']:
        date = datetime.fromtimestamp(day['dt']).strftime('%Y-%m-%d'),
        temp = day['temp']['day'],
        min_temp = day['temp']['min'],
        max_temp = day['temp']['max']

        cur.execute(f"INSERT kyunghyun7843.temp_weather_forecast VALUES ({date},{temp},{min_temp},{max_temp})")
        conn.commit()
    
    cur.close()
    conn.close()
    return None


def insert_recent_data(update_ver):
    conn = DB_HOOK.get_conn()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXIST kyunghyun7843.weather_forecast")

    if update_ver == 'incremental':
        cur.execute("""
                    create table kyunghyun7843.weather_forecast
                            AS SELECT date, temp, min_temp, max_temp, created_date
                                FROM (select ROW_NUMBER() OVER(
                                    PARTITION BY date ORDER BY created_date DESC), *
                                    FROM kyunghyun7843.temp_weather_forecast) seq
                                WHERE seq = 1;
                    """)
    elif update_ver == 'full':
       cur.execute(f"""
                    create table kyunghyun7843.weather_forecast
                            AS SELECT date, temp, min_temp, max_temp, created_date
                                FROM (select ROW_NUMBER() OVER(
                                    PARTITION BY date ORDER BY created_date DESC), *
                                    FROM kyunghyun7843.temp_weather_forecast) seq
                                WHERE seq = 1
                                ORDER BY created_date
                                LIMIT 7;
                    """)

    cur.execute("DROP TABLE IF EXIST kyunghyun7843.temp_weather_forecast")
    conn.commit()

    cur.close()
    conn.close()

with DAG(**dag_params) as dag:
    def _weather_forecast():
        lat, lon = get_geo_info()
        weather = get_weather(lat,lon)
        insert_forecast_to_temp(weather)
        insert_recent_data('incremental') #or full for full refresh
        return None
    
    weather_forecast = PythonOperator(
        task_id = 'weather_forecast',
        python_callable = _weather_forecast
    )

    weather_forecast 
