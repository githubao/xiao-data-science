#!/usr/bin/env python
# encoding: utf-8

"""
@description: 概率

@author: pacman
@time: 2017/9/30 18:40
"""

import math
import random


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


def run():
    conditional_boy_girl()


def main():
    run()


if __name__ == '__main__':
    main()
