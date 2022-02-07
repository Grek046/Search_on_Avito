import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

rezult = []

zapros = input('Введите запрос - ')

link = "https://www.avito.ru/rossiya/"

driver = webdriver.Chrome()
driver.maximize_window()
page = driver.get(link)

#имитируем ввод нашего запроса в поисковике авито
driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)

time.sleep(5)

ads = driver.find_elements(By.CLASS_NAME, "iva-item-content-rejJg")
urls = []
for ad in ads[0:3]:
    a = ad.get_attribute('href')
    url = {
        'href': a
    }
    urls.append(url)
    print(urls)

# name = driver.find_element(By.CLASS_NAME, 'title-root-zZCwT').text
# price = driver.find_element(By.CLASS_NAME, 'price-text-_YGDY').text
# id = driver.find_element(By.ID, 'i2316124193').text
# print(name)
# print(price)
# print(id)

# ob = driver.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')
# ob.click() #открываем объявление
# # НУЖНО ПОНЯТЬ КАК СЧИТАТЬ НОВУЮ СТРАНИЦУ И ПАРСИТЬ С НЕЁ
# soup = BeautifulSoup(driver.page_source, 'lxml')
# name = soup.find('span', class_='title-info-title-text')
# print(name)
# print(id)

# soup = BeautifulSoup(driver.page_source, 'lxml')
# ads = soup.findAll('div',class_='iva-item-titleStep-pdebR')
# for ad in ads[0:3]:
#     name = ad.find('h3', class_='title-root-zZCwT').text.strip()
#     # ob = driver.find_element(By.CSS_SELECTOR, '#i2258432180 > div > div.iva-item-aside-GOesg')
#     ob = driver.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')
#     ob.click() #открываем объявление
#     st = BeautifulSoup(driver.page_source, 'lxml')
#     elements = st.findAll('div',class_='item-view-search-info-redesign')
#     for el in elements:
#         # id = el.find('snap')
#         id = driver.find_element(By.TAG_NAME, 'span').text
#
#     # id = st.find('snap', class_='js-item-price')
#     # ss = driver.find_element(By.LINK_TEXT, name).get_attribute('href') #ссылка на каждое объявление
#     rezult.append([name,id])
#     # rezult.append(id)
#     # rezult.append(name)
#     # rezult.append(ss)
# print(rezult)



# селениум, подтягивает непонятный формат
# ads = driver.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
# for ad in ads:
#     name = ad.find_element(By.TAG_NAME, "h3")
#     print(name)



# spisok = driver.find_elements(By.NAME, 'itemprop')
# for i in range(len(spisok)):
#     print(spisok[i].text)




# def main():
#     pass
#
# #создал точку входа и вызвал функию main
# if __name__ == '__main__':
#     main()






