# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

"""for循环"""
"""求1-100之间的偶数和"""
# sum = 0
# for i in range(2, 101, 2):
#     sum += i
#
# print(sum)


"""while"""
"""
猜数字小游戏
人猜出计算机出的1-100之间的随机的数字
计算机给出一定的提示
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("please input an number:"))
    if number > answer:
        print("more smaller")
    elif number < answer:
        print("more bigger")
    else:
        print("congratulations!!!")
        break

print("the amount of your guessing:", counter)
if counter > 7:
    print("your intelligence is lower")



