# import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

rezult = []

zapros = input('Введите запрос - ')

link = "https://www.avito.ru/rossiya/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link)

#имитируем ввод нашего запроса в поисковике авито
driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'lxml')
ads = soup.findAll('div',class_='iva-item-titleStep-pdebR')
for ad in ads:
    name = ad.find('h3', class_='title-root-zZCwT').text.strip()
    rezult.append(name)
print(rezult[0:10])



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






