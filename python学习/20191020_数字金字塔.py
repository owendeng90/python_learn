#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 15:19
# @Author  : owen
# @Site    : 
# @File    : 20191020_数字金字塔.py
# @Software: PyCharm Community Edition
# @Code thought

for numrows in range(1,10):
    print('')
    rsl=''
    for numcolumns in range(1,10):
        if numcolumns<=numrows:
            print(numcolumns, end=' ')
            rsl+=str(9-numcolumns+1)
    print("*8+%d=%s" %(numrows,rsl))

