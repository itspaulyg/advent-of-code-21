#!/usr/bin/python3

import sys

OPEN={'(','{','[','<'}
CLOSE={')','}',']','>'}
MAPPING={'(':')', '[':']', '{':'}', '<':'>'}
POINTS={'(':1, '[':2, '{':3, '<':4, None:0}

def corruption(line):

    syntax = []
    for char in line:
        if char in OPEN:
            syntax.append(char)
        if char in CLOSE:
            if syntax:
                check = syntax.pop(-1)
                if MAPPING[check] == char:
                    continue
                return char
            else:
                return char

def repair(line):

    syntax = []
    for char in line:
        if char in OPEN:
            syntax.append(char)
        if char in CLOSE:
            check = syntax.pop(-1)
            if MAPPING[check] == char:
                continue
            else:
                syntax.append(check)

    if not syntax: return None
    points = 0
    for char in reversed(syntax):
        points *= 5
        points += POINTS[char]

    return points


def main():

    incomplete = []
    for line in sys.stdin:
        if corruption(line.strip()):
            continue
        incomplete.append(line.strip())

    points = []
    for line in incomplete:
        p = repair(line)
        if p:
            points.append(p)

    points = sorted(points)
    print(points[len(points)//2])


if __name__ == '__main__':
    main()
