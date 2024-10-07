import sqlite3
import os

connection = sqlite3.connect("table_toys.db")
cursor = connection.cursor()
# cursor.execute(
#     '''CREATE TABLE "toys" (
# 	"id"	INTEGER,
# 	"Артикул"	TEXT,
# 	"Наименование"	TEXT,
# 	"Цена"	INTEGER,
# 	"Вид"	TEXT,
# 	"Выбор"	INTEGER,
# 	"Посмотреть"	INTEGER,
# 	PRIMARY KEY("id")
# )''')
res = cursor.execute('SELECT * FROM toys')
# res = cursor.execute('SELECT COUNT(articul) FROM toys')
# res = cursor.execute('PRAGMA table_info("TEST")')
print(res.fetchall()[0][0])