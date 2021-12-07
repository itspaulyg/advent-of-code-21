#!/usr/bin/python3

import sys


def main():

    for line in sys.stdin:
        fishes = list(map(int, line.strip().split(',')))

    count = [0 for _ in range(10)]
    for fish in fishes:
        count[fish] += 1

    for _ in range(256):
        for i, val in enumerate(count):
            if i == 9:
                count[i] = 0
                continue
            if i == 0:
                count[7] += val
                count[9] += val
            count[i] = count[i + 1]

    print(sum(count))


if __name__ == '__main__':
    main()
