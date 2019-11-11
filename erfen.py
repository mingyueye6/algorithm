# coding: utf-8
# 二分查找算法

ls = list(range(100))

def binary_search(ls, num):
    # print(ls)
    mid = len(ls) // 2
    if len(ls) >= 1:
        if ls[mid] > num:
            binary_search(ls[:mid], num)
        elif ls[mid] < num:
            binary_search(ls[mid:], num)
        else:
            print(num)
            return num
    else:
        return None

binary_search(ls, 22)