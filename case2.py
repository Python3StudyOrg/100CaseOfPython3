#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time   : 2020/7/10 17:37
# @Author : Eastonliu
# @Desc   :
"""
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

分析：
1、输入的利润为profit
2、判断profit处于哪个奖金区间
3、profit减去奖金区间的下限值再乘以这个区间的提成
4、设置profit等于步骤3中的区间下限值
5、循环2,3,4步骤
6、把每个区间的提成相加
"""
profit = int(input("Please input profit:"))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(len(arr)):
    if profit > arr[i]:
        bonus += (profit - arr[i]) * rate[i]
        profit = arr[i]
print('bonus:%s' % bonus)
