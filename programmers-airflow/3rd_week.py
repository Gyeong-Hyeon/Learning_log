import psycopg2

host = 'learnde.cduaw970ssvt.ap-northeast-2.redshift.amazonaws.com'
port = '5439'
user = 'kyunghyun7843'
password = 'Kyunghyun7843!1'
dbname = 'dev'

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=dbname
)

cur = conn.cursor()
print(cur)