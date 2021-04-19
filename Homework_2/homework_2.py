import requests
import pickle
import json
from pprint import pprint
from bs4 import BeautifulSoup as bs
from fp.fp import FreeProxy
from time import sleep
import pandas as pd


url = 'https://moscow.hh.ru/vacancies/product_manager'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}


file_path ='hh_product!manager_vacancy.json'
proxies = {'https': f"{FreeProxy().get()}"}

pages = 0
file_list = []
while pages <= 39:
    sleep(0.5)
    r = requests.get(url, headers=headers, proxies=proxies)
    if r.status_code < 300:

        r.encoding = 'utf-8'
        file_list.append(r.text)
        try:
            soup = bs(r.text, 'html.parser')
            next_bottom = soup.find(attrs={'data-qa': "pager-block"})
            buttom_url = next_bottom.find('a')
            a = buttom_url.attrs['href']
            nex_page_url = f"https://moscow.hh.ru{a}"
            url = nex_page_url
            pages += 1
            print(pages)
            pprint(file_list)
        except Exception:
            print('error')
    else:
        print(r.status_code)

with open(file_path, 'wb') as f:
    pickle.dump(file_list, f)



with open(file_path, 'rb') as f:
    req = pickle.load(f)

vacancy = []
for b in req:
    soup = bs(b, 'html.parser')
    vacancy_list = soup.find_all(attrs={'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})

    for item in vacancy_list:
        info = {}
        a = item.find('a')
        selary = item.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
        if selary is None:
            info['salary'] = 'not declare'
        else:
            b = str(selary.text)
            clear_text = b.replace('\u202f', '')
            info['salary'] = clear_text
        info['Vacancy TITLE'] = a.text
        info['Vacancy URL'] = a.attrs['href']
        info['site path'] = url
        vacancy.append(info)

df = pd.DataFrame.from_records(vacancy)
data_cv = df.to_csv('Product_vacansy.csv')







