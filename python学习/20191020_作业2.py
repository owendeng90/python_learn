#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 10:59
# @Author  : owen
# @Site    : 
# @File    : 20191020_作业2.py
# @Software: PyCharm Community Edition
# @Code thought

numlist = input("请输入6个整数，并用空格分隔\n").split(" ")
numcolumns=0

while numcolumns<len(numlist):
    sum = 0
    numrows = 0
    while numrows<=numcolumns:
        sum += int(numlist[numrows])
        if numrows!=numcolumns:
            print("%d + " %int(numlist[numrows]),end='')
        else:
            print("%d = %d" %(int(numlist[numrows]),sum))
        numrows+=1
    numcolumns+=1