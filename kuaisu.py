# coding: utf-8
# 快速排序算法

ls = [11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]

def quick_sort(ls):
    if len(ls) < 2:
        return ls
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = ls[len(ls) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    ls.remove(mid)
    for item in ls:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


print(quick_sort(ls))