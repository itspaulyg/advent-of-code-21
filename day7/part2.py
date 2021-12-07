#!/usr/bin/python3

import sys
import statistics as s
import math

def main():

    crab_pos = list(map(int,input().strip().split(',')))
    target = math.floor(s.mean(crab_pos))
    fuel = 0
    for crab in crab_pos:
        fuel_used = 1
        while abs(crab-target):
            fuel += fuel_used
            fuel_used += 1
            crab = crab - 1 if crab > target else crab + 1
            
    print(fuel)


if __name__ == '__main__':
    main()
