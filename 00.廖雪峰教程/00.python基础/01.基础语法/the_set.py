#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

s2.add(6)
print(s2)

s2.remove(2)
print(s2)



# 可变和不可变 list 可变 而 str 不可变
a = 'abc'
b = a.replace('a', 'A') # 这里是重新创建了一个对象
print(b)
print(a)# a 保持了不变