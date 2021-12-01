#!/usr/bin/python3

import sys


def three_measures(measures):

    increased = 0
    prev = 2<<10
    for i in range(2, len(measures)):
        three_m = measures[i]+measures[i-1]+measures[i-2]
        if three_m > prev:
            increased += 1
        prev = three_m

    return increased


def main():

    measures = list()
    for line in sys.stdin:
        line = int(line.strip())
        measures.append(line)

    print(three_measures(measures))


if __name__ == '__main__':
    main()
