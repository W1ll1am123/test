import requests
from bs4 import BeautifulSoup


# def parsing():
#     headers = {
#         "Accept": "*/*",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0)"
#     }
#     link = "https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA&f=ASgBAgECAkSSA8YQygiAWQFFgqESECLQmtGD0L3RhtC10LLQviI"
#     response = requests.get(link, headers= headers)
#     soup = BeautifulSoup(response.content,  'html.parser')
#     print(soup.text)
#     # data = soup.find('a', {'data-marker': "item-title"}).text
#     # return data
#
# if __name__ == '__main__':
#     parsing()

from bs4 import BeautifulSoup  # для парсинга старниц
import requests  # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random

# url1 = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=1&room1=1'
# url = 'https://www.cian.ru'
# url2 = 'https://api.cian.ru/ebc-analytics/event-enrichment/'
#
# print(get(url))
# html_soup = BeautifulSoup(get(url).text, 'html.parser')
# print(html_soup)
# print(get(url).text)
# html_soup = BeautifulSoup(get(url).text, 'html.parser')
# print(requests.options(url2))
houses = []
count = 1
headers = {'Sec-Ch-Ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform':
"Windows",
'Sec-Fetch-Dest':
'empty',
'Sec-Fetch-Mode':
'cors',
'Sec-Fetch-Site':
'same-site',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36'}
while count <= 5:
    url = 'https://www.avito.ru/moskva/kvartiry/prodam/1-komnatnye-ASgBAgICAkSSA8YQygiAWQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA&p=' + str(count)
    print(url)
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', {'class': "iva-item-body-KLUuy"})
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1

print(len(houses))
print(houses[0])
print()
n = int(len(houses)) - 1
count = 0
while count <= 5:  # count <= n
    info = houses[int(count)]
    price = info.find('meta',{'itemprop':'price'})
    title = info.find('a', 'href')
    print(title, ' ', price)
    count += 1