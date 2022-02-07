import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


zapros = input('Введите запрос - ')

link = "https://www.avito.ru/rossiya/"

driver = webdriver.Chrome()
driver.maximize_window()
page = driver.get(link)

driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)
time.sleep(10)

ads = driver.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
urls = []
for ad in ads[0:10]:
    name = ad.find_element(By.CLASS_NAME, 'title-root-zZCwT').text.strip()
    url_ad = ad.find_element(By.LINK_TEXT, name).get_attribute('href')
    links = {
        'href': url_ad
    }
    urls.append(links)
for url in urls:
    driver.get(url['href'])
    id = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/div[2]/div[1]/div/div[5]/span').text
    price = driver.find_element(By.CLASS_NAME, 'js-item-price').text
    date = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item-redesign').text
    author = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/div[2]/div[1]/div/div[4]/div/div/div[1]/div[1]/div/a').text
    address = driver.find_element(By.CLASS_NAME, 'item-address-georeferences').text
    views = driver.find_element(By.CLASS_NAME, 'title-info-metadata-item').text
    print(id)
    print(price)
    print(date)
    print(author)
    print(address)
    print(views)
