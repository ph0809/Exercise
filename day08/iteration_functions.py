# -*- coding: utf-8 -*-
# -*- author: ph -*-

"""1.  range"""
names = ['a', 'b', 'c', 'd']
ages = [1, 2, 3, 4]

# for i in range(len(names)):
#     print(names[i], 'is', ages[i], 'years old')
#
# # 可以直接使用下面的写法
# b = zip(names, ages)   # 可以应付不等长序列，以短的用完为止
# print(b)
# for name,age in b:
#     print(name, 'is', age, 'years old')


"""2.  enumerate"""
# 遍历一个可遍历的数据对象（列表，元组或者字符串），同时列出数据和下标
# for i, name in enumerate(names):
#     print(i, name)


"""3.  sorted  &  reversed"""
# list1 = [43,23,65,44,7,100,22,99,32]
# print(list1.sort(reverse=False))
# print(sorted(list1 ,reverse=True))
# print(reversed('hello world'))


"""4.  break跳出循环"""
# from math import sqrt
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break


"""5.  continue"""
while True:
    word = input('please enter a word:')
    if not word:
        break
    print('the word is '+word)






