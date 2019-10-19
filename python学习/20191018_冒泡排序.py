#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 17:14
# @Author  : owen
# @Site    : 
# @File    : 20191018_冒泡排序.py
# @Software: PyCharm Community Edition
# @Code thought
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 22:30
# @Author  : owen
# @Site    :
# @File    : 20191018_02.py
# @Software: PyCharm Community Edition
# @Code thought
#生成一个包含20个0到100的随机整数的列表，然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变
import random

numlist = []
for i in range(20):
    num=random.randint(1,100)
    numlist.append(num)
length=len(numlist)

for i in range(int(length/2)):
    for j in range(0, int(length/2)-i-1):
            if numlist[j*2] > numlist[j*2 + 2]:
                numlist[j*2], numlist[j*2 + 2] = numlist[j*2 + 2], numlist[j*2]
