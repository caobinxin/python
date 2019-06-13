#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO) # 这个是控制 log 的输出等级

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)