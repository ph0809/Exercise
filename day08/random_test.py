# -*- coding: utf-8 -*-
# -*- author: ph -*-
from random import *
import random


"""1.伪随机数列生成模块"""
# a = Random()
# a.seed(1)   # 使用相同的seed, 可以获取完全相同的随机数序列
# list1 = [a.randint(1, 100) for i in range(20)]
#
# print(list1)


"""2.正太分布函数"""
# random.normalvariate(mu=None, sigma=None)   # mu是平均数，sigma是标准差


"""3.打乱一个列表中的元素"""
# random.shuffle(x=None, random=None)
list2 = random.shuffle([3,4,5,6,72,1])

"""4.待更新"""


