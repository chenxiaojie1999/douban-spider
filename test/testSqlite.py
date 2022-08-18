# -*- coding: utf-8 -*-
"""
@Time       : 2022/08/17 10:49
@Author     : bonnie
@FileName   : testSqlite.py
@Description: 
"""

import sqlite3

#2.创建数据表
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件

print("成功打开数据库")

c = conn.cursor()  # 获取游标

sql = '''
    create table company
        (id int primary key not null,
        name test not null,
        age int not null,
        address char(50),
        salary real);
'''

c.execute(sql)  # 执行SQL语句
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据库

print("成功建表")



