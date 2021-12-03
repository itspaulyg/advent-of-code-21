#!/usr/bin/python3

import sys


def find_most_common(diagnostics, i):

    common = 0
    for binary in diagnostics:
        if binary[i] == '0':
            common += 1

    if common > len(diagnostics) / 2:
        return '0', '1'
    else:
        return '1', '0'


def main():

    diagnostics = list()
    for line in sys.stdin:
        diagnostics.append(line.strip())

    gamma = ''
    epsilon = ''
    for i in range(len(diagnostics[0])):
        temp1, temp2 = find_most_common(diagnostics, i)
        gamma += temp1
        epsilon += temp2 

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma*epsilon)

if __name__ == '__main__':
    main()
