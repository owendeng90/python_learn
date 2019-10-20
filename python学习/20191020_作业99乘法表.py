#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 11:21
# @Author  : owen
# @Site    : 
# @File    : 20191020_作业99乘法表.py
# @Software: PyCharm Community Edition
# @Code thought
numlist = input("请输入9个整数(1-9)，并用空格分隔\n").split(" ")


for num in numlist:
    print(num,end='  ')
print('')
for num in numlist:
    print("---",end='')
for numrows in range(1,10):
    print('')
    print('%d|'%numrows,end='')
    for numcolumns in range(1,10):
        rsl=numcolumns*numrows
        print(rsl,end=' ')



