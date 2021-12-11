#!/usr/bin/python3

import sys

OPEN={'(','{','[','<'}
CLOSE={')','}',']','>'}
MAPPING={'(':')', '[':']', '{':'}', '<':'>'}
POINTS={')':3, ']':57, '}':1197, '>':25137, None:0}

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

def main():

    points = 0
    for line in sys.stdin:
        points += POINTS[corruption(line.strip())]

    print(points)


if __name__ == '__main__':
    main()
