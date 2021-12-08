#!/usr/bin/python3

import sys
from itertools import permutations

SEGMENT={2,3,4,7}

def count_unique(output, decoder):

    values = list(decoder.values())
    count = ''
    for num in output:
        for c in permutations(num, len(num)):
            c = "".join(c)
            if c in values:
                count += str(list(decoder.keys())[values.index(c)])

    return int(count)


def decode(numbers):

    DECODE = {
        1: numbers[0],
        4: numbers[2],
        7: numbers[1],
        8: numbers[-1]
    }

    while(len(DECODE) != 10):
        for num in numbers:
            flag = True
            if num in DECODE.values():
                continue
            sz = len(num)
            if sz == 5:
                for let in DECODE[1]:
                    if let not in num:
                        flag = False
                        break
                if flag:
                    DECODE[3] = num
                else:
                    flag = True
                    count = 0
                    for let in DECODE[4]:
                        if let in num:
                            count += 1
                    if count == 3:
                        DECODE[5] = num
                    else:
                        DECODE[2] = num
            if sz == 6:
                for let in DECODE[4]:
                    if let not in num:
                        flag = False
                        break
                if flag:
                    DECODE[9] = num
                else:
                    flag = True
                    for let in DECODE[1]:
                        if let not in num:
                            flag = False
                            break
                    if flag:
                        DECODE[0] = num
                    else:
                        DECODE[6] = num
    return DECODE

def main():

    total = []
    for line in sys.stdin:
        line = line.strip().split('| ')
        numbers = line[0].strip().split()
        numbers = sorted(numbers, key=lambda s: len(s))
        decoder = decode(numbers)
        output = line[-1].split()
        total.append(count_unique(output, decoder))
    print(sum(total))

if __name__ == '__main__':
    main()
