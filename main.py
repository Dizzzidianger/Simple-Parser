import pandas as pd
import requests
from bs4 import BeautifulSoup

# запрос на сайт
url = 'https://murmansk.rabota.ru/'
r = requests.get(url)

# статус код 
r.raise_for_status()


#поиск заголовков вакансий с нумерацией

soup = BeautifulSoup(r.text, 'lxml')
titles = soup.find_all('h3' )

for index , title in enumerate(titles, start= 1):
    title = title.text
    print (f"{index}.{title}")


