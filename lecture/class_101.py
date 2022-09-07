import requests
from utils import connect_url, extract_class_text, extract_herf_by_class, calculate_duration

# CATEGORIES = ['9','a']
CATEGORIES = ['9']

HEADER = ('site','category','title','lecturer','price','duration','tags','url')
DATA = []

for category in CATEGORIES:
    url = f'https://class101.net/plus/ko/categories/62206086d39299379ee5b83{category}'
    window = connect_url(url, False, True)
    # titles = extract_class_text(window, 'css-p2s8cv')
    # lecturers = extract_class_text(window, 'css-1gctxks')
    hrefs = extract_herf_by_class(window, 'css-kvfwce')
    for href in hrefs:
        url = href + '?tap=curriculum'
        window = requests.get(url)
        time = calculate_duration(window, 'p', 'css-6t5aq4')
    """
    calculate_duration함수 테스트부터 작업
    """
    