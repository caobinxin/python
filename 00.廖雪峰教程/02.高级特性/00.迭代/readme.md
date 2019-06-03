Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？

因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，也就是说有多少事可知的。但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。

 

判断是不是可以迭代，用Iterable


 from collections import Iterable  

isinstance({}, Iterable) --> True  

isinstance((), Iterable) --> True  

isinstance(100, Iterable) --> False  

 

 

判断是不是迭代器，用Iterator

 

from collections import Iterator  

isinstance({}, Iterator)  --> False  

isinstance((), Iterator) --> False  

isinstance( (x for x in range(10)), Iterator)  --> True  


所以，

 

凡是可以for循环的，都是Iterable

凡是可以next()的，都是Iterator

集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象

Python中的for循环就是通过next实现的


- 最大的区别就是，迭代器事先不知道要迭代多少次， 而可迭代是事先知道要迭代多少次的

