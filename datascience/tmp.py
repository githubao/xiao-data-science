#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试

@author: pacman
@time: 2017/9/30 15:24
"""

def tmp():
    arg = [1,2]
    # print(multiply(arg))
    # 多个参数的拆包操作
    print(multiply(*arg))

def tmp2():
    print(list(map(add_one, [1, 2, 3])))
    print(list(map(multiply, [1, 2, 3], [4, 5, 6])))
    print(list(map(sum_all, [1, 2], [3, 4],[5,6] )))


def tmp1():
    dic = {1: 2}
    for k, v in dic.items():
        print(k, v)

def add_one(x):
    return x + 1

def multiply(x, y):
    return x * y

def sum_all(*args):
    return sum(args)

def main():
    tmp()


if __name__ == '__main__':
    main()
