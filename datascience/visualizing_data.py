#!/usr/bin/env python
# encoding: utf-8

"""
@description: 数据可视化 

@author: pacman
@time: 2017/9/30 16:06
"""

import matplotlib.pyplot as plt
from collections import Counter


def make_chart_simple_line_chart():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title('Normal GDP')
    plt.ylabel('Billions of $')
    plt.show()


def make_chart_simple_bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    xs = [i + 0.1 for i, _ in enumerate(movies)]

    plt.bar(xs, num_oscars)
    plt.title('# of Academy Awards')
    plt.title('My Favorite Movies')

    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

    plt.show()


def make_chart_histogram():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)
    plt.axis([-5, 105, 0, 5])

    plt.xticks([10 * i for i in range(11)])
    plt.xlabel('Decile')
    plt.ylabel('# of Students')

    plt.title('Distribution of Exam 1 Grades')
    plt.show()


def make_chart_misleading_y_axis(mislead=True):
    mentions = [500, 505]
    years = [2013, 2014]

    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years)
    plt.ylabel('# of times I heard someone say "data science"')

    plt.ticklabel_format(useOffset=False)

    if mislead:
        plt.axis([2012.5, 2014.5, 499, 506])
        plt.title('Look at the "Huge" Increase!')
    else:
        plt.axis([2012.5, 2014.5, 0, 550])
        plt.title('Not So Huge Anumore.')

    plt.show()


def make_chart_several_line_charts():
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]

    xs = range(len(variance))

    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')

    # plt.legend(loc=9)
    plt.xlabel('model complexity')
    plt.title('The Bias-Variance Tradeoff')

    plt.show()


def make_chart_scatter_plot():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords='offset points')

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()


def make_chart_scatterplot_axes(equal_axes=False):
    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")

    if equal_axes:
        plt.title("Axes Are Comparable")
        plt.axis("equal")
    else:
        plt.title("Axes Aren't Comparable")

    plt.show()


def make_chart_pie_chart():
    plt.pie([0.95, 0.05], labels=['Uses pie charts', 'Knows better'])

    plt.axis('equal')
    plt.show()


def main():
    # make_chart_simple_line_chart()
    # make_chart_simple_bar_chart()
    # make_chart_histogram()
    # make_chart_misleading_y_axis(False)
    # make_chart_several_line_charts()
    # make_chart_scatter_plot()
    # make_chart_scatterplot_axes(True)
    make_chart_pie_chart()


if __name__ == '__main__':
    main()
