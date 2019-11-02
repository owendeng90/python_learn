#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 23:58
# @Author  : owen
# @Site    : 
# @File    : 20191103_reverse_case.py
# @Software: PyCharm Community Edition
# @Code thought
import random

str=input('请输出字符串\n')
strlist=list(str)
strlistlen=len(strlist)
outstr=''
i=0

while i<strlistlen:
    if strlist[i].isupper():
        outstr+=strlist[i].lower()
    else:
        outstr += strlist[i].upper()
    i += 1
print(outstr)