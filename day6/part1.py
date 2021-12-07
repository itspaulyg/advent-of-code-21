#!/usr/bin/python3

import sys


def main():

    for line in sys.stdin:
        fishes = list(map(int, line.strip().split(',')))
    for i in range(80):
        for j, fish in enumerate(fishes):
            if fish == 0:
                fishes[j] = 6
                fishes.append(9)
            else:
                fishes[j] -= 1

    print(len(fishes))



if __name__ == '__main__':
    main()
