import requests
import pickle
import json
from pprint import pprint
from bs4 import BeautifulSoup as bs
from fp.fp import FreeProxy

url = 'https://moscow.hh.ru/vacancies/product_manager'
headers = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
proxies = {'https': f"{FreeProxy().get()}"}




file_path ='hh_product!manager_vacancy.json'

r = requests.get(url, headers=headers, proxies=proxies)


if r.status_code < 300:
    r.encoding = 'utf-8'
    with open(file_path, 'wb') as f:
        pickle.dump(r.text, f)
else:
    print(r.status_code)

with open(file_path, 'rb') as f:
    req = pickle.load(f)

print(req.text)

