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

insertnum=random.randint(1,1000)

for i in range(0,numcnt):
    small_flg=i
    for j in range(i+1,numcnt+1):
        if list[small_flg]>list[j]:
            small_flg=j
    list[i],list[small_flg]=list[small_flg],list[i]
print(list)