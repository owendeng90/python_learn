#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 11:32
# @Author  : owen
# @Site    : 
# @File    : 20191020_while星号输出.py
# @Software: PyCharm Community Edition
# @Code thought

for numrows in range(1,7):
    print('')
    for numcolumns in range(1,7):
        if numcolumns<=numrows:
            print(numcolumns,end=' ')