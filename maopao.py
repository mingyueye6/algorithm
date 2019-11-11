# coding: utf-8
# 冒泡排序算法

ls = [2, 6, 8, 1, 5, 7, 3, 9]

n  = len(ls)

# 升序
for i in range(n):
    for j in range(n - i -1):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]

print(ls)

# 降序
for i in range(n):
    for j in range(n - i - 1):
        if ls[j] < ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]

print(ls)