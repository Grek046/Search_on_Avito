import sqlite3

conn = sqlite3.connect('data_base.db')

#создаём SQL запрос
sql = "CREATE TABLE ads (id TEXT, title TEXT, price TEXT, date TEXT, author TEXT, address TEXT, views TEXT, description TEXT, photo TEXT)"
sql = "SELECT * FROM ads"

cursor = conn.cursor()
cursor.execute(sql)

res = cursor.fetchall()
for r in res:
    print(r)
    # print("id: ", r[0])
    # print("Название: ", r[1])

conn.close()