import requests
from utils import connect_url, extract_class_text

# CATEGORIES = ['programming','datascience']
CATEGORIES = ['programming']
HEADER = ('site','category','title','lecturer','price','duration','tags','url')
DATA = []

for category in CATEGORIES:
    url = f'https://fastcampus.co.kr/category_online_{category}'
    resp = requests.get(url).text
    print(resp.find('dev_online_befinal'))

    window = connect_url(url)
    title = extract_class_text(window, 'card__title')
    desc = extract_class_text(window,'card__content')
    tags = extract_class_text(window, 'card__labels')
