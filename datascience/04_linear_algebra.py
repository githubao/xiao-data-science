#!/usr/bin/env python
# encoding: utf-8

"""
@description: 线性代数

@author: pacman
@time: 2017/9/30 17:16
"""

from functools import reduce
import math
import matplotlib.pyplot as plt

def vector_add(v, w):
    return [i + j for i, j in zip(v, w)]


def vector_subtract(v, w):
    return [i - j for i, j in zip(v, w)]


def scalar_multiply(c, v):
    return [c * i for i in v]


def vector_mean(vectors):
    return scalar_multiply(1 / len(vectors), vector_sum(vectors))


def vector_sum(vectors):
    return reduce(vector_add, vectors)


def dot(v, w):
    return sum(i * j for i, j in zip(v, w))


# 平方和
def sum_of_squares(v):
    return dot(v, v)


# 平方根
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def square_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(square_distance(v, w))


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A):
    pass


def get_column(A):
    pass


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def matrix_add(A, B):
    def func(i, j):
        return A[i][j] + B[i][j]

    return make_matrix(*shape(A), func)


def is_diagonal(i, j):
    return 1 if i == j else 0

def make_graph_dot_product_as_vector_projection():
    v = [2, 1]
    w = [math.sqrt(.25), math.sqrt(.75)]
    c = dot(v, w)
    vonw = scalar_multiply(c, w)
    o = [0,0]

    plt.arrow(0, 0, v[0], v[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("v", v, xytext=[v[0] + 0.1, v[1]])
    plt.arrow(0 ,0, w[0], w[1],
              width=0.002, head_width=.1, length_includes_head=True)
    plt.annotate("w", w, xytext=[w[0] - 0.1, w[1]])
    plt.arrow(0, 0, vonw[0], vonw[1], length_includes_head=True)
    plt.annotate(u"(v•w)w", vonw, xytext=[vonw[0] - 0.1, vonw[1] + 0.1])
    plt.arrow(v[0], v[1], vonw[0] - v[0], vonw[1] - v[1],
              linestyle='dotted', length_includes_head=True)
    plt.scatter(*zip(v,w,o),marker='.')
    plt.axis('equal')
    plt.show()


def tmp():
    res = [(i, j) for i in range(3) for j in range(3, 6)]
    print(res)


def run():
    vectors = [[1, 2, 3], [4, 5, 6]]
    vectors2 = [[2, 3, 4], [5, 6, 7]]
    # print(vector_sum(vectors))
    # print(vector_mean(vectors))
    # print(matrix_add(vectors, vectors2))
    make_graph_dot_product_as_vector_projection()


def main():
    run()
    # tmp()


if __name__ == '__main__':
    main()
