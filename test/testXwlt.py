# -*- coding: utf-8 -*-
"""
@Time       : 2022/08/14 21:49
@Author     : bonnie
@FileName   : testXwlt.py
@Description: 
"""
import random

import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")  # 创建word book对象
# worksheet = workbook.add_sheet('sheet1')  # 创建工作表
# worksheet.write(0, 0, 'hello')  # 写入数据，第一行参数“行”，第二行参数“列”，第三个参数内容
# workbook.save('student.xls')  # 保存数据表

workbook = xlwt.Workbook(encoding="utf-8")  # 创建word book对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表

jieguo = 0
for i in range(0, 9):
    for j in range(0, i+1):
        jieguo = i+1 * j+1
        worksheet.write(i, j, "%d * %d = %d" % (i+1, j+1, jieguo))
workbook.save('student.xls')  # 保存数据表