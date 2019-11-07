#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 22:18
# @Author  : owen
# @Site    : 
# @File    : 20191022_直接插入排序.py
# @Software: PyCharm Community Edition
# @Code thought

import random

numcnt=15
list=[]
for i in range(numcnt+1):
    list.append(random.randint(1,1000))

for i in range(1,numcnt+1):
    key=list[i]
    j=0
    while j<i:
        if key<list[j]:
            list[i],list[j]=list[j],list[i]
        j+=1
print(list)

