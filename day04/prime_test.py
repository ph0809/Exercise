# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

"""判断一个整数是否是素数"""
from math import sqrt

num = int(input("please input "))
end = int(sqrt(num))
is_prime = True
for i in range(2, end+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('true', num)
else:
    print('false', num)

