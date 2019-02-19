#!/usr/bin/python3

# pip3 install pymysql

import pymysql

db = pymysql.connect("localhost", "root", "Feng123456", "mytest")
cursor = db.cursor()
sql = "INSERT INTO test(id, name) \
       VALUES ('%s', '%s')" % \
      (3, 'Mohan')
# update insert delete ,sql is different only
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()