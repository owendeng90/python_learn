#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 8:28
# @Author  : owen
# @Site    :
# @File    : test.py
# @Software: PyCharm Community Edition
# @Code thought

number=7
i=1

while i<number:
    j=number-i
    while j>0:
        print(' ', end=' ')
        j-=1

    x=i
    while x>0:
        print('*', end=' ')
        x-=1

    y=i
    while y>1:
        print('*', end=' ')
        y -= 1
    print('')
    i+=1
