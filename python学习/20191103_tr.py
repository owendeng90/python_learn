#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 15:58
# @Author  : owen
# @Site    : 
# @File    : 20191103_tr.py
# @Software: PyCharm Community Edition
# @Code thought

def tr(srcstr, dststr, inputstring):
    outputstring=inputstring
    srcstrlist=list(srcstr)
    dststrlist = list(dststr)
    i=0
    while i< len(list(srcstr))-len(list(dststr)):
        dststrlist.append('')
        i+=1
    replace_dict=dict(zip(srcstrlist,dststrlist))
    stringlist=list(inputstring)
    for intputchar in stringlist:
        if intputchar in replace_dict:
            outputstring=outputstring.replace(intputchar,replace_dict[intputchar])
    return outputstring

print(tr(srcstr= 'abcdef', dststr= 'mno', inputstring= 'abcdefghi'))

