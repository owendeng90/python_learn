#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 16:08
# @Author  : owen
# @Site    : 
# @File    : 20191102_string.py
# @Software: PyCharm Community Edition
# @Code thought

import keyword

inputstring=input("输出字符串\n")
stringlen=len(inputstring)

print('lenth of string is %d' %stringlen)
if stringlen==1:
    print('then string lenth is 1')
else:
    print('then string lenth not is 1')
if inputstring in keyword.kwlist:
    print('the string is keyword')
else:
    print('the string is not keyword')
