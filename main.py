from flask_primer import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sqlite3
import time


app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///parsing.db'
db = SQLAlchemy(app)

class Table(db.Model):
    ad = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Table %r>' % self.ad   #будет выдаваться сам объект и его ad (порядковый номер)

link = "https://www.avito.ru/rossiya/"
zapros = input('Введите запрос - ')


@app.route('/')
def service():
    return "Для начала поиска добавьте к адресной строке: /search"


@app.route('/create_table')
def create_table():


@app.route('/search')
def pars():
    driver = webdriver.Chrome()
    driver.get(link)

    driver.find_element(By.TAG_NAME, "label").send_keys(zapros + Keys.ENTER)
    time.sleep(3)

    rezult = []
    urls = []
    ads = driver.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
    for ad in ads[0:3]:
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
        title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text.strip()
        id = driver.find_element(By.XPATH, "//div[@class='item-view-search-info-redesign']//span").text
        # rezult_ad = {
        #     'id': id,
        #     'title': title
        # }
        rezult.append((id, title))

    conn = sqlite3.connect('data_base.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO ads VALUES (?,?)", rezult)
    conn.commit()
    conn.close()

    return rezult





# def connect_db():
#     conn = sqlite3.connect('b_base.db')
#     conn.row_factory = sqlite3.Row  #возвращает данные из БД в виде словаря
#     return conn

# def main():
#     pass
#
# #создал точку входа и вызвал функию main
if __name__ == '__main__':
    app.run()






