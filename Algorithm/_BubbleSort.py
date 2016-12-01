#coding=utf-8

'''
需求: 冒泡排序
原理: 比较相邻的两个元素,如果前一个比后一个大,就交换位置
'''

def bubble_sort(arr):
    length = len(arr)
    # 第一级遍历
    for i in range(length):
        # 第二级遍历
        for j in range(1, length - i):
            if arr[j - 1] > arr[j]:
                # 交换两者数据
                # temp = arr[j - 1]
                # arr[j - 1] = arr[j]
                # arr[j] = temp
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    print(arr)

bubble_sort('列表')

