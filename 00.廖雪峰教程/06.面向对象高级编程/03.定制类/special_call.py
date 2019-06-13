#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()



# 那么，怎么判断一个变量是对象还是函数呢？
# 其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们
# 上面定义的带有__call__()的类实例：

print(callable(Student('cao')))

print(callable(max))

print(callable([1, 2, 3]))

print(callable(None))

print(callable('str')) 