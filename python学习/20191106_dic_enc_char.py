#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 23:16
# @Author  : owen
# @Site    : 
# @File    : 20191106_dic_enc_char.py
# @Software: PyCharm Community Edition
# @Code thought

def rot13(inputstring):
    outputstring=''
    rot_list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for inputchar in list(inputstring):
        if inputchar.isalpha() and inputchar.upper()==inputchar:
            if rot_list.index(inputchar.lower())+13<25:
                index_enc = rot_list.index(inputchar.lower()) + 13
            else:
                index_enc= rot_list.index(inputchar.lower()) -13
            outputstring+=rot_list[index_enc].upper()
        elif inputchar.isalpha() and inputchar.upper()!=inputchar:
            if rot_list.index(inputchar)+13<25:
                index_enc =rot_list.index(inputchar)+13
            else:
                index_enc = rot_list.index(inputchar) -13
            outputstring+=rot_list[index_enc]
        else:
            outputstring += inputchar
    return outputstring

inputstring=input('% rot13.py Enter string to rot13:\n')
print('Your string to en/decrypt was:[%s]' %inputstring)
outputstring=rot13(inputstring)
print('The rot13 string is:[%s]' %outputstring)