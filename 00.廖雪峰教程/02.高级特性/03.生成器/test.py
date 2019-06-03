#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(max):
    x = -1
    while x < max:
        print("yield before")
        yield x
        print("yield after")
        x = x + 1
    return 'caobinxin' # 要指定  #!/usr/bin/env python3 在开头，不然会报错


f = func(3)
for x in f:
    print("for: %d" % x)