#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5)) # 将列表生成式中的 [] 换成 （） 就变成生成器
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(10)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

#要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，
# 并在适当的条件结束for循环。对于函数改成的generator来说，
# 遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。

#请注意区分普通函数和generator函数，普通函数调用直接返回结果：
#generator函数的“调用”实际返回一个generator对象：