#!/usr/bin/python3

import sys


def main():

    horizontal = 0
    depth = 0
    aim = 0
    for line in sys.stdin:
        cmd = line.strip().split()
        if cmd[0] == "forward":
            horizontal += int(cmd[1])
            depth += aim*int(cmd[1])
        elif cmd[0] == "down":
            aim += int(cmd[1])
        elif cmd[0] == "up":
            aim -= int(cmd[1])

    print(horizontal*depth)


if __name__ == "__main__":
    main()
