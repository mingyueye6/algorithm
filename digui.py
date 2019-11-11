# coding: utf-8
# 斐波那契数列[1,1,2,3,5,8,13,21,34,55]

# 递归算法
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

fib_num = fib(10)
print(fib_num)

# 递推算法
def fib_list(n):
    ls = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        ls.append(a)
    return ls

fib_ls = fib_list(20)
print(fib_ls)
