# import requests
# from bs4 import BeautifulSoup as bs
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sqlite3
from pprint import pprint

zapros = input('Введите запрос - ')
link = "https://www.avito.ru/rossiya/"

driver = webdriver.Chrome()
driver.maximize_window()
page = driver.get(link)

driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)
time.sleep(3)

rezult = []
urls = []
ads = driver.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
for ad in ads[0:5]:
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

    # title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text.strip()
    # try:
    #     button = driver.find_element(By.XPATH, "//button[@data-marker='item-phone-button/card']")
    #     button.click()
    # except:
    #     button = 'Номер не указан'
    # при поиске номера в разных категориях за кнопку отвечают разные теги (/button телефоны и мебель и /a авто и недвижимость)

    # time.sleep(5)

    id = driver.find_element(By.XPATH, "//div[@class='item-view-search-info-redesign']//span").text
    title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text.strip()
    date = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item-redesign').text
    try:
        views = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item').text
    except:
        views = "Количество просмотров не указано"
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
    # добавляю в кортеж все результаты
    rezult.append((id, title, price, date, author, address, views, description, photo))


# Создаю словари с информацией и помещаю в общий список
    # rezult_ad = {
    #     'id': id,
    #     'title': title,
    #     'price': price,
    #     'date': date,
    #     'author': author,
    #     'address': address,
    #     'views': views,
    #     'description': description,
    #     'photo': photo,
    # }
    # rezult.append(rezult_ad)
# pprint(rezult)

conn = sqlite3.connect('data_base.db')
cursor = conn.cursor()
cursor.executemany("INSERT INTO ads VALUES (?,?,?,?,?,?,?,?,?)", rezult)
conn.commit()

sql = "SELECT * FROM ads"

cursor = conn.cursor()
cursor.execute(sql)

res = cursor.fetchall()
for r in res:
    print(r)
    # print("id: ", r[0])
    # print("Название: ", r[1])

conn.close()


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