# import requests
# from bs4 import BeautifulSoup as bs
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

zapros = input('Введите запрос - ')

link = "https://www.avito.ru/rossiya/"

driver = webdriver.Chrome()
driver.maximize_window()
page = driver.get(link)
time.sleep(3)

driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)
time.sleep(3)

rezult = []
urls = []
ads = driver.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
for ad in ads[0:2]:
    try:
        block = ad.find_element(By.CLASS_NAME, 'title-root-zZCwT').text.strip()
        url_ad = ad.find_element(By.LINK_TEXT, block).get_attribute('href')
        links = {
            'href': url_ad
        }
        urls.append(links)
    except:
        continue

for url in urls:
    driver.get(url['href'])
    time.sleep(3)
    id = driver.find_element(By.XPATH, "//div[@class='item-view-search-info-redesign']//span").text
    title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text.strip()
    date = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item-redesign').text
    views = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item').text
    photo = url['href'] + "#extended"
    try:
        price = driver.find_element(By.CLASS_NAME, 'js-item-price').text
    except:
        price = 'Цена не указана'
    try:
        author = driver.find_element(By.XPATH, "//div[@class='seller-info-name js-seller-info-name']//a").text
    except:
        author = 'Имя автора - не указано'
    try:
        address = driver.find_element(By.CLASS_NAME, 'item-address__string').text
    except:
        address = 'Адрес не указан'
    try:
        description = driver.find_element(By.CLASS_NAME, 'item-description').text.strip()
    except:
        description = 'Без описания'
    time.sleep(2)

    rezult_ad = {
        'ID': id,
        'Title': title,
        'price': price,
        'date': date,
        'author': author,
        'address': address,
        'views': views,
        'description': description,
        'photo': photo
    }
    rezult.append(rezult_ad)
pprint(rezult)

# json_rezult = json.dumps(rezult, indent=3)  # в формате unicod, нужно почитать как и исправить
# print(json_rezult)

    # print(id)
    # print(title)
    # print(price)
    # print(date)
    # print(author)
    # print(address)
    # print(views)
    # print(description)
    # print(photo)
    # print()
    # print()