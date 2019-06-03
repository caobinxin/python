#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9) # 这种属于 闭包，将 args参数列表先保存下来
print(f)
print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# 由于这里的 i 是一个变量， f执行的时候，已经 i == 3
print(f1())
print(f2())
print(f3())

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i)) # 注意 这里是 f() 是执行的意思，此时 j 是 1 2 3
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())