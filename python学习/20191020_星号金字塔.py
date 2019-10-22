#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 14:58
# @Author  : owen
# @Site    : 
# @File    : 20191020_星号金字塔.py
# @Software: PyCharm Community Edition
# @Code thought

num = int(input("请星号金字塔层数\n"))

for numrows in range(1,2*num):
    print('')
    for numcolumns in range(1,2*num):
        if numrows<=num and numcolumns>=num-(numrows-1) and numcolumns<=num+(numrows-1):
            print('*',end=' ')
        elif numrows > num and numcolumns > numrows-6+1 and numcolumns < 2*num -(numrows-6+1):
            print('*', end=' ')
        else:
            print(' ',end=' ')