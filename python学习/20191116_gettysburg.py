#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 23:20
# @Author  : owen
# @Site    : 
# @File    : 20191116_gettysburg.py
# @Software: PyCharm Community Edition
# @Code thought

# gettysburg.txt是一个文件文件，请用函数，list,dict,文件读写等知识分析该文本文件中单词个数（输出所有单词，并输出个数），
# 输出不重复的单词和个数， 统计每个单词出现的次数，并输出单词和出现次数的表。

f=open('F:\\学习内容\\python学习\\gettysburg.txt','r')
dict_str={}
for line in f.readlines():
    line_list=line.split()
    for line_str in line_list:
        word = line_str.lower()
        word_cnt = 1
        if word in dict_str:
            dict_str[word]=dict_str[word]+1
        else:
            dict_str_update = {word:word_cnt}
            dict_str.update(dict_str_update)
print(dict_str)