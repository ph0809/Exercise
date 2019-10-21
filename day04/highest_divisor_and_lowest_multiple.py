# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

num1 = int(input("please input num1:"))
num2 = int(input("please input num2:"))

if num1 > num2:
    """如果num1大于num2的值，则交换"""
    num1, num2 = num2, num1

for i in range(num1, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print("%d,%d的最大公约数是：%d"%(num1, num2, i))
        print("%d,%d的最小公倍数是：%d"%(num1, num2, num1*num2//i))
        break

