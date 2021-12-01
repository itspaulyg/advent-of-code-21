#!/usr/bin/python3

import sys


def main():

    increased = 0
    prev = 2<<10
    for line in sys.stdin:
        line = int(line.strip())
        if line > prev:
            increased += 1
        prev = line

    print(increased)


if __name__ == '__main__':
    main()
