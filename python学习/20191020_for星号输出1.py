#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 11:48
# @Author  : owen
# @Site    : 
# @File    : 20191020_for星号输出1.py
# @Software: PyCharm Community Edition
# @Code thought


#类型3
numrows=1
while numrows <=6:
    print('')
    numcolumns=6
    while numcolumns >0:
        if numcolumns<=numrows:
            print(numcolumns,end=' ')
        else:
            print(' ',end=' ')
        numcolumns-=1
    numrows += 1

#类型2
# numrows=6
# while numrows >=0:
#     print('')
#     numcolumns=1
#     while numcolumns <=6:
#         if numcolumns<=numrows:
#             print(numcolumns,end=' ')
#         numcolumns+=1
#     numrows -= 1


#类型1
# numrows=1
# while numrows <=6:
#     print('')
#     numcolumns=1
#     while numcolumns <=6:
#         if numcolumns<=numrows:
#             print(numcolumns,end=' ')
#         numcolumns+=1
#     numrows += 1