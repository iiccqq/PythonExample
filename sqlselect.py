#!/usr/bin/python3

# pip3 install pymysql

import pymysql

db = pymysql.connect("localhost", "root", "Feng123456", "mytest")
cursor = db.cursor()
sql = "SELECT id,name from test ";
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        print("id=%s,name=%s" %(id, name))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()