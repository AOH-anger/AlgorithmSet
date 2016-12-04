#coding=utf-8
'''
需求: 归并算法
原理:
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2.设定两个指针，最初位置分别为两个已经排序序列的起始位置
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4.重复步骤3直到某一指针到达序列尾
5.将另一序列剩下的所有元素直接复制到合并序列尾

模块介绍
Deque模块是Python标准库collections中的一项. 它提供了两端都可以操作的序列, 这意味着可以在序列前后都执行添加或删除.
'''
from collections import deque

def merge_sort(arr):
    # c长度判断
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) // 2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)

def merge(left,right):
    # 创建对象
    merged,left,right = deque(),deque(left),deque(right)
    while left and right:
        merged.append(left.popleft() if left[0] < right[0] else right.popleft())
    merged.extend(left if left else right)
    return  list(merged)
