#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 16:44
# @Author  : owen
# @Site    : 
# @File    : 20191102_string_sort.py
# @Software: PyCharm Community Edition
# @Code thought


strlist = input("请输出字符串用空格分隔\n").split()
strlist.sort(reverse=False)
print(strlist)