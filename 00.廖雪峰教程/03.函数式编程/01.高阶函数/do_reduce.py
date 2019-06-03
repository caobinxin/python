#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        if n == -1:
            point = 1
            # print("point=%d: f=%d n=%d" % (point, f, n))
            return f
        if point == 0:
            # print("point=%d: f=%d n=%d" % (point, f, n))
            
            return f * 10 + n
        else:
            # print("point=%d: f=%d n=%d" % (point, f, n))
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0) #第三个参数是一个 初始化的值， 0 或者 0.0 都是可以的，如果是0.0会被自动 转成整数0

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


# reduce 有 三个参数

# function 	有两个参数的函数， 必需参数
# sequence 	tuple ，list ，dictionary， string等可迭代物，必需参数
# initial 	初始值， 可选参数