# -*- coding: utf-8 -*-
# -*- author: ph -*-

"""将一个正整数逆序输出"""
a = int(input("please input an number:"))
# result = True
# while result:
#     i = a % 10
#     a = a // 10
#     print(i)
#     if a//10 == 0:
#         print(a)
#         result = False


reversed_num = 0
while a > 0:
    reversed_num = reversed_num*10 + a % 10
    a = a // 10
print(reversed_num)





