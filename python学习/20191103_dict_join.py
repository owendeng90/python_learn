#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 9:26
# @Author  : owen
# @Site    : 
# @File    : 20191103_dict_join.py
# @Software: PyCharm Community Edition
# @Code thought

dict_a={'a':1,'b':2,'c':3}
dict_b={'d':4,'e':5,'f':6}
dict_c={}
dict_c.update(dict_a)
dict_c.update(dict_b)
print(dict_c)
