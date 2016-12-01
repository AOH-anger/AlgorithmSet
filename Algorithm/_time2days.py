#coding=utf-8
'''
输入年月日,判断是这一年的第几天
'''

def isLeap(year):
    '''
        判断输入的年份是否为闰年
    '''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def isValidDay(year, month, day):
    '''
        判断输入的某年某月某日是不是一个合法的天数
    '''
    dayofMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year):
        dayofMonth[2] = 29  # 如果是闰年，则相应的2月份改为29天
    return dayofMonth[month] >= day  # 如果输入的day大于当月对应的天数，则day非法


def daysOfYear(year, month, day):
    '''
        计算某年某月某日是这一年的第多少天
    '''
    # 定义一个列表，下标对应月份，下标所对应的元素代表截止到当月底，距离年初一共有多少天
    days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    # 判断月份是否合法
    if month <= 0 or month > 12:
        print('input error')
        return 0

    # 判断天数是否合法
    if not isValidDay(year, month, day):
        print('input error')
        return 0

    '''
        这句代码当输入的日期是闰年的2月29号时，也会出错
        if (isLeap(year) and month == 2 and day > 29) or day > dayofMonth[month] or day<=0:
            print('input error')
            return 0
    '''
    # 要求month月第day天是year年的第多少天，只需求先求出month-1月底距离年初多少天，然后再加上day即可
    res = days[month - 1] + day

    # 以上是非闰年的情况，如果year是闰年，则需要天数再加1
    if month > 2 and isLeap(year):
        res += 1

    return res


def main():
    # 让用户输入数据
    year = int(input('please input the year:'))
    month = int(input('please input the month:'))
    day = int(input('please input the day:'))

    days = daysOfYear(year, month, day)

    print("days:%d" % days)


if __name__ == "__main__":
    main()
