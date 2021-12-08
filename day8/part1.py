#!/usr/bin/python3

import sys

SEGMENT={2,3,4,7}

def count_unique(output):

    count = 0
    for num in output:
        if len(num) in SEGMENT:
            count += 1

    return count


def main():

    count = 0
    for line in sys.stdin:
        output = line.strip().split('| ')[-1].split()
        count += count_unique(output)

    print(count)

if __name__ == '__main__':
    main()
