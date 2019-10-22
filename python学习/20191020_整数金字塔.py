#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 11:48
# @Author  : owen
# @Site    :
# @File    : 20191020_for星号输出1.py
# @Software: PyCharm Community Edition
# @Code thought

num = int(input("请输入任意整数(1-15)\n"))

for numrows in range(1,num+1):
    print('')
    for numcolumns in range(1,2*num):
        if numcolumns>=num-(numrows-1) and numcolumns<=num+(numrows-1):
            if numcolumns==num:
                print(1,end=' ')
            elif numcolumns<num:
                print(6-numcolumns+1, end=' ')
            else:
                print(numcolumns-6+1, end=' ')
        else:
            print(' ',end=' ')