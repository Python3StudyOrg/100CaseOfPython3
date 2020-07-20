#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time   : 2020/7/20 16:26
# @Author : Eastonliu
# @Desc   :

"""
输入三个整数x,y,z，请把这三个数由小到大输出。

"""

# 第一种方法：sort函数
# seq = []
# for i in range(3):
#     num = input("please input %dth number:" % (i + 1))
#     seq.append(num)
# seq.sort()
# print(seq)


# 第二种方法：冒泡排序法
# seq = []
# for i in range(3):
#     num = input("please input %dth number:" % (i + 1))
#     seq.append(num)
# for i in range(len(seq) - 1):
#     for j in range(len(seq) - i - 1):
#         if seq[j] > seq[j + 1]:
#             seq[j], seq[j + 1] = seq[j + 1], seq[j]
# print(seq)


# 第三种方法：选择排序法
seq = []
for i in range(3):
    num = input("please input %dth number:" % (i + 1))
    seq.append(num)
for i in range(len(seq) - 1):
    min_index = i
    for j in range(i + 1, len(seq)):
        if seq[j] < seq[min_index]:
            min_index = j
    seq[min_index], seq[i] = seq[i], seq[min_index]
print(seq)
