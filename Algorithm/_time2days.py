#coding=utf-8
'''
输入年月日,判断是这一年的第几天
'''

def isLeap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def daysOfYear(year, month, day):
    dayofMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    # 判断用户输入
    if month <= 0 or month > 12:
        print('input error')
        return 0

    if (isLeap(year) and month == 2 and day > 29) or day > dayofMonth[month] or day <= 0:
        print('input error')
        return 0

    # 计算时间
    res = days[month - 1] + day

    if month > 2 and isLeap(year):
        res += 1

    return res


def main():
    # 用户输入数据
    year = int(raw_input('please input the year:'))
    month = int(raw_input('please input the month:'))
    day = int(raw_input('please input the day:'))

    days = daysOfYear(year, month, day)

    print("days:%d" % days)

if __name__ == "__main__":
    main()