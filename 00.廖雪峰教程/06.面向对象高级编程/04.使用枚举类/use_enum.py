#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 =', day1)
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)



CBX = Enum('c',( 'b', 'x'))

print('member.value ==> ',CBX.b.value)
print('member.value ==> ',CBX['b'].value)

print('member ==> ',CBX.b)
print('member ==> ',CBX['b'])

for name, member in CBX.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class CY(Enum):
    chen = 0
    yang = 1
    cao = 2
    bin = 3
    xin = 4

for name, member in CY.__members__.items():
    print(name, '=>', member, ',', member.value)