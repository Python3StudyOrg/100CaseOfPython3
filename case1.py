#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time   : 2020/7/10 17:28
# @Author : Eastonliu
# @Desc   :

"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i*100+j*10+k)
