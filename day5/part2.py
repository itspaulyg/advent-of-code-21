#!/usr/bin/python3

import sys


def mark_grid(grid, p1, p2, xy):

    # x values the same 
    if xy == 0:
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        for i in range(y1, y2+1):
            grid[p1[0]][i] += 1
    # y values the same 
    elif xy == 1:
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for i in range(x1, x2+1):
            grid[i][p1[1]] += 1
    # diagonal
    elif xy == 2:
        x = p1[0]
        y = p1[1]
        diff = abs(p1[0] - p2[0])
        inc_x = False if p1[0] > p2[0] else True
        inc_y = False if p1[1] > p2[1] else True
        for _ in range(diff+1):
            grid[x][y] += 1
            x += 1 if inc_x else -1
            y += 1 if inc_y else -1


def check_grid(grid):

    overlap = 0
    for i in grid:
        for j in i:
            if j > 1:
                overlap += 1

    return overlap


def main():

    grid = [[0 for i in range(1000)] for i in range(1000)]

    for line in sys.stdin:
        line = line.strip().split(' -> ')
        p1 = tuple(map(int, line[0].split(',')))
        p2 = tuple(map(int, line[1].split(',')))
        if p1[0] == p2[0]:
            mark_grid(grid, p1, p2, 0)
        elif p1[1] == p2[1]:
            mark_grid(grid, p1, p2, 1)
        else:
            mark_grid(grid, p1, p2, 2)

    print(check_grid(grid))


if __name__ == '__main__':
    main()
