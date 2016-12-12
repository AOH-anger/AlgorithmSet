'''
需求:
获取二进制中1的个数
'''

def  getOne(value):
    count = 0
    #数字的二进制表示中有多少个1就进行多少次操作
    while value != 0:
        count += 1
        # 从最右边的1开始，每一次操作都使n的最右的一个1变成了0，即使是符号位也会进行操作。
        value = value&(value-1)
    print (count)

getOne(7)
