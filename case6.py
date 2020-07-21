#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time   : 2020/7/21 14:26
# @Author : Eastonliu
# @Desc   :
"""
斐波那契数列。
"""


def fib(n):
    """
    打印前n个斐波那契数列
    :param n:
    :return:
    """
    f1 = 0
    f2 = 1
    seq = [f1, f2]
    if n <= 0 or not isinstance(n, int):
        return None
    if n == 1:
        return [f1]
    if n == 2:
        return seq
    for i in range(3, n + 1):
        count = f1 + f2
        seq.append(count)
        f1, f2 = f2, count
        i += 1
    return seq


if __name__ == '__main__':
    print(fib(5.6))
