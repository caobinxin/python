#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)




# 只读属性
class People(object):

    @property
    def name(self):
        print('getname...')
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be an str')
        self._name = value

    @property
    def age(self):
        return 10


p = People()
p.name = 'cbx'
print(p.name)

p.age = 100 # 这里是只读



    
    