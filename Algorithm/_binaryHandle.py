#coding=utf-8

'''
需求:
二进制类型的简单的操作
1: 不使用三方变量交换两个整数变量的值
2: 交换二进制数中 i和 j位的值
3: 64位整型数的二进制表示形式倒转
'''

#需求一 交换两个整型变量的值  ===============================================================
def exchangeValue(x,y):
    # 省略边界判断

    #  one 使用逻辑运算符
    # x = x ^ y
    # y = x ^ y
    # x = x ^ y

    #  two 使用python运算赋值规则(交换多个变量的值也是可以的)
    x,y= y,x
    print ('x = %s y = %s' %(x,y))


#需求二 交换二进制数中 i 和 j 位的值  =======================================================
def changeBinary(x,i,j):
    # 省略边界判断

    '''
    1: 获取i 和 j位的值
    2: 将i 和 j位的值互换
    '''
    if ((x >> i) & 1) != ((x >> j) & 1):
        x ^=  (1 << i) | ( 1 << j)
    print (x)


# 需求三 二进制表示形式的倒转  ==============================================================
# 参考资料: http://mikewell.lofter.com/post/1cc590dd_83385f0
# 参考资料: https://zhidao.baidu.com/question/549823293.html
def reverseBinary(x):
    #省略边界判断

    m = bin(x)[2:][::-1] # 将整数x转换为二进制字符串
    n = int(m,base=2)
    print (n) # 利用int函数，字符串可以以0b为前缀，也可以不使用,函数会将输入base进制的字符串转换为十进制


#exchangeValue(9,10)
#changeBinary(5,1,0)
#reverseBinary(10)


