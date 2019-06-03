#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0))) # 按照 key 进行排序
print(sorted(students, key=lambda t: t[1])) # 按照 value 进行排序
print(sorted(students, key=itemgetter(1), reverse=True)) #按照 value进行排序 并且反序
