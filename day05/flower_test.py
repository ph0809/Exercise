# -*- coding: utf-8 -*-
# -*- author: ph -*-


"""水仙花数"""
for num in range(100, 1000):
    first = num % 10
    second = num // 10 % 10
    third = num // 100

    cnt = first ** 3 + second ** 3 + third ** 3
    if cnt == num:
        print(num)