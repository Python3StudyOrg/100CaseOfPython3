#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time   : 2020/7/13 11:38
# @Author : Eastonliu
# @Desc   :

"""
输入某年某月某日，判断这一天是这一年的第几天？
分析：
1、根据年份判断是否为闰年，闰年2月份为29天
2、把前n-1个月的天数相加
3、最后再加上天数就是一年中的第多少天
"""
month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
year = int(input('please year:'))
month = int(input('please month:'))
day = int(input('please day:'))
# 判断是否闰年，闰年2月份为29天
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    month_days[2] = 29
days = 0
for m in range(1, month):
    days += month_days.get(m)
days += day
print(days)
