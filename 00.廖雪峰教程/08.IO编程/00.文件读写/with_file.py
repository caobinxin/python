#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))
    f.write('\n')
    f.write('caobinxin\n')
    f.write('chenyang\n')

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f.readlines(): # 这里注意 使用的是 readlines  千万不能少了后面的s
        print(line.strip())