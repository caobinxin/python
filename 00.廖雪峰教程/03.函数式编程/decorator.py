#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # now = log(now)
def now():
    print('2015-3-25')

now()
print(now.__name__) # 屏蔽和打开 # @functools.wraps(func)，可以看到不同的效果

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，



def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG——曹斌鑫') # today = log('DEBUG——曹斌鑫')(today)
def today(s):
    print('2015-3-25 %s' % s)

today("hello")
print(today.__name__)


