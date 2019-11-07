#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 23:38
# @Author  : owen
# @Site    : 
# @File    : 20191103_num_eng.py
# @Software: PyCharm Community Edition
# @Code thought
import random

a=random.randint(0,1000)
strlist=list(str(a))
strlistlen=len(strlist)
engstr=''
num_eng = {'0': 'zero','1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
i=0

while i<strlistlen:
    if i<strlistlen-1:
        engstr+=num_eng[strlist[i]]+'-'
    else:
        engstr += num_eng[strlist[i]]
    i += 1
print(a)
print(engstr)
