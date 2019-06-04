#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    __name = 'Animal' # 私有成员
    def run(self):
        print('%s is running...' % self.__name)

class Dog(Animal):
    __name = 'Dog'

class Cat(Animal):
    __name = 'Cat'

class Pig(): # 这里没有继承任何一个类
    __name = 'Pig'

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c) # 变量应该不能多态，多态的是 函数

# 仔细看这里的pig 类的定义，他并没有继承任何一个类，
p = Pig()
# run_twice(p)

