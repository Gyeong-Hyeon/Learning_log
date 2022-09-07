import time
from datetime import timedelta
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def connect_url(url:str, need_sizing:bool=False, need_scroll:bool=False) -> webdriver:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--log-level=3') #warning 무시
    resp = requests.get(url)

    if resp.status_code != 200:
        print(resp.status_code)
        raise HTTPError
    window = webdriver.Chrome(
                                service=Service(ChromeDriverManager().install()),
                                options=options
                            )
    window.get(url)
    if need_sizing:
        #태그 다 가져오기 위해 브라우저 창 최대화
        window.set_window_size(4096,2160)

    if need_scroll:
        while True:
            prev_heigth = window.execute_script("return document.body.scrollHeight")
            # 아래로 스크롤
            window.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)  # 로딩이 올래 걸리는 사이트는 시간을 더 크게 잡아주자
            curr_height = window.execute_script("return document.body.scrollHeight")
            #스크롤해도 문서 기준 높이가 변하지 않으면 종료
            if prev_heigth == curr_height:
                break
            prev_heigth = curr_height
    return window

def extract_class_text(window:webdriver, class_name:str) -> list:
    #try:
    elems = window.find_elements(By.CLASS_NAME, class_name)
    return [elem.text for elem in elems]

def extract_herf_by_class(window:webdriver, class_name:str) -> list:
    parent_nodes = window.find_elements(By.CLASS_NAME, class_name)
    hrefs = []
    for parent_node in parent_nodes:
        href = parent_node.find_element(By.XPATH, './/a[@href]').get_attribute('href')
        hrefs.append(href)
    return hrefs

def calculate_duration(window:requests.Response, tag_type, class_name:str) -> str:
    def calculate_time(sum_time:timedelta, new_time:str) -> timedelta:
        new_times = new_time.split(':')
        if len(new_times) > 2:
            sum_time+=timedelta(hours=int(new_times[0]))
            new_times.pop(0)
        if len(new_times) > 1 :
            sum_time+=timedelta(minutes=int(new_times[0]))
            new_times.pop(0)
        return sum_time+timedelta(seconds=int(new_times[0]))

    elems = BeautifulSoup(window.content, 'html.parser').find_all(tag_type,class_=class_name)
    times = [elem.text for elem in elems]

    sum_time = timedelta(seconds=0)
    for t in times:
        sum_time = calculate_time(sum_time, t)
    return sum_time
