import time
from urllib.error import HTTPError
import requests
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

def extract_class_text(window:webdriver, elem_name:str, type:str='str') -> list:
    try:
        elems = window.find_elements(By.CLASS_NAME, elem_name)
        if type == 'str':
            return [elem.text for elem in elems]
        elif type == 'int':
            nums = [elem.get_attribute("value") for elem in elems]
            return sum(nums)
    except:
        """
        값 못찾는 경우 예외처리 해야함
        """
        return None

def extract_herf_by_class(window:webdriver, parent_elem:str) -> list:
    parent_nodes = window.find_elements(By.CLASS_NAME, parent_elem)
    hrefs = []
    for parent_node in parent_nodes:
        href = parent_node.find_element(By.XPATH, './/a[@href]').get_attribute('href')
        hrefs.append(href)
    return hrefs
