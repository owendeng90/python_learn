#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 11:32
# @Author  : owen
# @Site    : 
# @File    : 20191020_while星号输出.py
# @Software: PyCharm Community Edition
# @Code thought

num = input("请输入任意整数(1-15")

for numrows in range(1,2*num-1):
    print('')
    for numcolumns in range(1,2*num-1):
        if numcolumns<=num+1 and numcolumns<=num+1:
            print(numcolumns,end='')
        else:
            print(' ',end='')