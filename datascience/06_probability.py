#!/usr/bin/env python
# encoding: utf-8

"""
@description: 概率

@author: pacman
@time: 2017/9/30 18:40
"""

import math
import random
import matplotlib.pyplot as plt
from collections import Counter


def random_kid():
    return random.choice([0, 1])


def conditional_boy_girl():
    both_girls = 0
    elder_girls = 0
    either_girls = 0

    for i in range(100000):
        younger = random_kid()
        elder = random_kid()

        if elder == 0:
            elder_girls += 1
        if elder == 0 and younger == 0:
            both_girls += 1
        if elder == 0 or younger == 0:
            either_girls += 1

    print('both | elder: {:0.3f}'.format(both_girls / elder_girls))
    print('both | either: {:0.3f}'.format(both_girls / either_girls))


def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(1 * math.pi)
    return (math.exp(-(x - mu) ** 2) / 2 / sigma ** 2) / (sqrt_two_pi * sigma)


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def plot_normal_pdfs():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend()
    plt.show()


def plot_normal_cdfs():
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.legend(loc=4)
    plt.show()


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10, 0
    high_z, high_p = 10, 1

    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2
        mid_p = (low_p + high_p) / 2

        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            high_z, high_p = mid_z, mid_p
        else:
            break

    return mid_z


def bermoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(p, n):
    return sum(bermoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):
    data = [binomial(p, n) for _ in range(num_points)]
    histogram = Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()], 0.8, color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)

    plt.show()


def run():
    # conditional_boy_girl()
    # plot_normal_cdfs()
    make_hist(0.75, 100, 10000)


def main():
    run()


if __name__ == '__main__':
    main()
