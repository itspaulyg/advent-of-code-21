#!/usr/bin/python3

import sys


def find_basin(heightmap, row, num):

    # RECURSION ????


def find_low_points(heightmap):

    total = 0
    for row in range(1, len(heightmap)):
        for num in range(1, len(heightmap[row])-1):
            point = heightmap[row][num]
            if point < heightmap[row-1][num] and point < heightmap[row][num-1] and point < heightmap[row][num+1] and point < heightmap[row+1][num]:
                total += point + 1
                # TODO with lowpoint now find basin
                find_basin(heightmap, row, num)

    return total


def main():

    padding = [10 for _ in range(103)]
    heightmap = []
    heightmap.append(padding)
    for line in sys.stdin:
        entry = []
        entry.append(10)
        entry.extend(list(map(int,line.strip())))
        entry.append(10)
        heightmap.append(entry)
    heightmap.append(padding)

    print(find_low_points(heightmap))


if __name__ == '__main__':
    main()
