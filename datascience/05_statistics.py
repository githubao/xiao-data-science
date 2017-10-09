#!/usr/bin/env python
# encoding: utf-8

"""
@description: 统计学

@author: pacman
@time: 2017/9/30 17:41
"""

"""
辛普森悖论：比较数据的时候，一定要保证两份数据是可比较的！！！

"""

from datascience.linear_algebra import sum_of_squares, dot
import math
from collections import Counter
import matplotlib.pyplot as plt


def make_friends_count_histogram():
    friends_counts = Counter(num_friends)
    xs = range(101)
    ys = [friends_counts[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title('Histogram of friend Counts')
    plt.xlabel('# of friends')
    plt.xlabel('# of people')
    plt.show()


def simple_statistics():
    num_points = len(num_friends)  # 204

    largest_value = max(num_friends)  # 100
    smallest_value = min(num_friends)  # 1

    sorted_values = sorted(num_friends)
    smallest_value = sorted_values[0]  # 1
    second_smallest_value = sorted_values[1]  # 1
    second_largest_value = sorted_values[-2]


def mean(x):
    return sum(x) / len(x)


def median(v):
    n = len(v)
    sorted_v = sorted(v)

    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        return (sorted_v[midpoint] + sorted_v[midpoint - 1]) / 2


# 分位数
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [(x, count) for x, count in counts.items() if count == max_count]


def data_range(x):
    return max(x) - min(x)


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


def de_mean(x):
    x_bar = mean(x)
    return [i - x_bar for i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return math.sqrt(variance(x))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


# [-1,1] 完全负相关 到 完全正相关
def correlation(X, Y):
    std_x = standard_deviation(X)
    std_y = standard_deviation(Y)
    if std_x > 0 and std_y > 0:
        return covariance(X, Y) / std_x / std_y
    else:
        return 0


# 删除异常数据
def correlation_reinforce(X, Y):
    outlier = X.index(100)
    X_good = [x for i, x in enumerate(X) if i != outlier]
    Y_good = [x for i, x in enumerate(Y) if i != outlier]

    return correlation(X_good, Y_good)


def main():
    # make_friends_count_histogram()
    print(correlation(num_friends, daily_minutes))
    print(correlation_reinforce(num_friends, daily_minutes))


num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1]
daily_minutes = [1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, 54.01, 38.79, 47.59, 49.1,
                 27.66, 41.03, 36.73, 48.65, 28.12, 46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73, 40.57, 31.65, 31.21,
                 36.32, 20.45, 21.93, 26.02, 27.34, 23.49, 46.94, 30.5, 33.8, 24.23, 21.4, 27.94, 32.24, 40.57, 25.07,
                 19.42, 22.39, 18.42, 46.96, 23.72, 26.41, 26.97, 36.76, 40.32, 35.02, 29.47, 30.2, 31, 38.11, 38.18,
                 36.31, 21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28, 24.17, 22.31, 30.17, 25.53, 19.85, 35.37, 44.6,
                 17.23, 13.47, 26.33, 35.02, 32.09, 24.81, 19.33, 28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51,
                 15.23, 39.72, 40.8, 26.06, 35.76, 34.76, 16.13, 44.04, 18.03, 19.65, 32.62, 35.59, 39.43, 14.18, 35.24,
                 40.13, 41.82, 35.45, 36.07, 43.67, 24.61, 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59, 27.53,
                 13.82, 33.2, 25, 33.1, 36.65, 18.63, 14.87, 22.2, 36.81, 25.53, 24.62, 26.25, 18.21, 28.08, 19.42,
                 29.79, 32.8, 35.99, 28.32, 27.79, 35.88, 29.06, 36.28, 14.1, 36.63, 37.49, 26.9, 18.58, 38.48, 24.48,
                 18.95, 33.55, 14.24, 29.04, 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2, 32.01, 29.27, 33, 13.74,
                 20.42, 27.32, 18.23, 35.35, 28.48, 9.08, 24.62, 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22,
                 34.65, 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42, 9.82, 23.39, 30.93, 15.03, 21.67,
                 31.09, 33.29, 22.61, 26.89, 23.48, 8.38, 27.81, 32.35, 23.84]

if __name__ == '__main__':
    main()
