#!/usr/bin/python3

import sys


def find_most_common(diagnostics, i):

    if len(diagnostics) == 1:
        return diagnostics[0]

    common = 0
    for binary in diagnostics:
        if binary[i] == '0':
            common += 1

    leftovers = list()
    if common > len(diagnostics) / 2:
        for binary in diagnostics:
            if binary[i] == '0':
                leftovers.append(binary)
    else:
        for binary in diagnostics:
            if binary[i] == '1':
                leftovers.append(binary)

    return find_most_common(leftovers, i + 1)


def find_least_common(diagnostics, i):

    if len(diagnostics) == 1:
        return diagnostics[0]

    common = 0
    for binary in diagnostics:
        if binary[i] == '0':
            common += 1

    leftovers = list()
    if common <= len(diagnostics) / 2:
        for binary in diagnostics:
            if binary[i] == '0':
                leftovers.append(binary)
    else:
        for binary in diagnostics:
            if binary[i] == '1':
                leftovers.append(binary)

    return find_least_common(leftovers, i + 1)


def main():

    diagnostics = list()
    for line in sys.stdin:
        diagnostics.append(line.strip())

    oxygen = find_most_common(diagnostics, 0)
    co2 = find_least_common(diagnostics, 0)
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    print(oxygen*co2)

if __name__ == '__main__':
    main()
