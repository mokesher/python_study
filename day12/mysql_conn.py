#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='hxmh23',db="testdb")

cursor = conn.cursor()
# 执行sql，并返回行数、数据
# effect_row = cursor.execute("select * from student")
# print(effect_row)
# print(cursor.fetchall())

data = [
    ("n1","2018-04-07","m"),
    ("n2","2018-04-07","m"),
    ("n3","2018-04-07","m"),
]

cursor.executemany("insert into student (name,register_date,sex) values (%s,%s,%s)",data)

conn.commit()           #默认开启事务，数据保存需要提交