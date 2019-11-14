# -*- coding: utf-8 -*-
# -*- author: ph -*-


class A():
    name = 'jessie'
    age = 25

    def apple(self):
        print('i like apple')

    def conut(self, n):
        print(n*n)

"""1. setattr(object, name, value)"""
a = A()
setattr(a, "sex", 'male')
print(a.sex)

"""2. getattr(object, name, value)"""
print(getattr(a, 'name'))
print(getattr(a, 'num', 0))

"""3. hasattr(object, name, value)"""
print(hasattr(a, 'name'))
print(hasattr(a, 'num'))
