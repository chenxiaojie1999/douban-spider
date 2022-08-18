# -*- coding: utf-8 -*-
"""
@Time       : 2022/08/13 12:32
@Author     : bonnie
@FileName   : testRe.py
@Description: 
"""

# 正则表达式：字符串模式（判断字符串是否符合一定的标准

import re

# 创建模式对象
# pat = re.compile("AA")  # 此处的AA，是正则表达式，用来验证其他的字符串
# m = pat.search("CBA")  # search字符串被校验的内容
# m = pat.search("CBAA")  # search字符串被校验的内容

# 没有对象模式
m = re.search("asd", "aaasd")

print(re.findall("a","ADdaaajoefndsjfksfkjakj"))
print(re.findall("[A-Z]","AEFRHYJFYFsdzdgtergtARFERGE"))

#sub

print(re.sub("a","A","asdasfdfaddddddddfa"))

print(m)
