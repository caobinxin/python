#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    def carnivor(self):
        print('Carnivor...')


# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass



