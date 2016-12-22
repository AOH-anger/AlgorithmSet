#coding=utf8

'''
需求:
素数判断

思路:
解法1: 使用暴力枚举
解法2: 判断一个数是否是素数,只要看小于它的素数是否能整除它即可
解法3: 使用筛除法: 拿到一个素数,然后将素数倍数对应的数全都删除,例如拿到2,将2的倍数全部删除
'''

import math

def isPrime():

    # 初始化一个x大小的列表,全部初始化为 1 (True / False)
    a = [1 for x in range(0, 101)]

    # 如果不是素数, 则将 a 中对应的 1 修改为 0
    for i in range(2, 101):  # math.sqrt(x) 返回x的平方根
        if a[i] == 1:
            for j in range(i * 2, 101, i):  #从 i*2 到 201 , 间隔 i
                a[j] = 0

    # 打印所有的素数
    for i in range(1, 101):
        if a[i] == 1:
            print(i)
isPrime()