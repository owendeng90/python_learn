#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 17:20
# @Author  : owen
# @Site    : 
# @File    : 20191103_random_set.py
# @Software: PyCharm Community Edition
# @Code thought
import random

num_n=random.randint(1,100)
num_list=[]
for i in range(num_n):
    num_list.append(random.randint(1,2**31-1))

num_chose_n=random.randint(1,100)
if num_chose_n>num_n:
    num_chose_n=num_n

num_chose_list=[]
for i in range(num_chose_n):
    j=random.randint(0,len(num_list)-1)
    num_chose_list.append(num_list[j])
num_chose_list.sort()
print(num_chose_list)

