#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:29
# @Author  : owen
# @Site    : 
# @File    : 20191103_dict_reverse_key_value.py
# @Software: PyCharm Community Edition
# @Code thought

dict_a={'e':4,'d':5,'a':6,'f':1,'b':2,'c':3}
dict_a_value=list(dict_a.values())
dict_a_key=list(dict_a.keys())
dict_a_reverse = dict(zip(dict_a_value,dict_a_key))

