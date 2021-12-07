#!/usr/bin/python3

import sys
import statistics as s

def main():

    crab_pos = list(map(int,input().strip().split(',')))
    target = s.median(crab_pos)
    fuel = 0
    for crab in crab_pos:
        fuel += abs(crab-target)

    print(int(fuel))


if __name__ == '__main__':
    main()
