import requests
from utils import connect_url, extract_class_text, extract_herf_by_class

# CATEGORIES = ['9','a']
CATEGORIES = ['9']

HEADER = ('site','category','title','lecturer','price','duration','tags','url')
DATA = []

for category in CATEGORIES:
    url = f'https://class101.net/plus/ko/categories/62206086d39299379ee5b83{category}'
    window = connect_url(url, False, True)
    # title = extract_class_text(window, 'css-p2s8cv')
    # lecturer = extract_class_text(window, 'css-1gctxks')
    # hrefs = extract_herf_by_class(window, 'css-kvfwce')
    time = extract_class_text(window, 'css-6t5aq4', 'int')
    """
    utils.py에서 00:00 -> time형태로 형변환하는 코드부터 작업해야함
    """
    