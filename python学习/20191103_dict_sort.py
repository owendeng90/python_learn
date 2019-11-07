#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 10:07
# @Author  : owen
# @Site    : 
# @File    : 20191103_dict_sort.py
# @Software: PyCharm Community Edition
# @Code thought

dict_a={'e':4,'d':5,'a':6,'f':1,'b':2,'c':3}
print('#按键排序并输出')
for k in sorted(dict_a):
    print(k,dict_a[k])

print('#按值排序并输出')
for k in sorted(dict_a,key=dict_a.__getitem__):
    print(k,dict_a[k])