# AlgorithmSet
Using python to achieve a variety of algorithms

# 1. _time2days.py
##需求:

输入某年某月某日，判断这一天是这一年的第几天？

# 2. _judge2power.py
##需求：

实现一个方法，判断一个正整数是否是2的乘方。要求性能尽可能高。

##解析:

1: 将正整数转换为二进制

2: 2的乘方的二进制形式都是只有最高位是1,其余是 0

3: 将转换后的二进制全部 -1 , 整个数减少一位, 其他位由0变为1

4: 将2的乘方本身和它减一后的数进行 位与运算 , 结果等于 0

参考资料: http://blog.jobbole.com/107689/