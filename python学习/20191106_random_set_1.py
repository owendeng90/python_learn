#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 0:02
# @Author  : owen
# @Site    : 
# @File    : 20191106_random_set_1.py
# @Software: PyCharm Community Edition
# @Code thought
import random

num_chose_a=random.randint(1,10)
num_chose_b=random.randint(1,10)
num_n_set_a=set()
num_n_set_b=set()
for i in range(num_chose_a):
    num_n=random.randint(0,9)
    num_n_set_a.add(num_n)

for i in range(num_chose_b):
    num_n=random.randint(0,9)
    num_n_set_b.add(num_n)

print(num_n_set_a)
print(num_n_set_b)
print(num_n_set_a|num_n_set_b)
print(num_n_set_a&num_n_set_b)


