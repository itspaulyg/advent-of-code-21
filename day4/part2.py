#!/usr/bin/python3

import sys
from bingo import Board, Number


def bingo_time(numbers, boards):

    winners = set()
    for num in numbers:
        for b in boards:
            b.mark_number(num)
            if b.check_board():
                winners.add(b)
                if len(winners) == len(boards):
                    return b, int(num)


def main():

    numbers = sys.stdin.readline().strip()
    numbers = numbers.split(',')

    boards = list()
    board = list(list())
    count = 0
    for line in sys.stdin:
        if line == '\n':
            continue
        if count % 5 == 0 and board:
            b = Board(board, False)
            boards.append(b)
            board = list(list())
        row = list(map(Number, line.strip().split()))
        board.append(row)
        count += 1

    board, num = bingo_time(numbers, boards)
    total = board.sum_unmarked()
    print(total * num)


if __name__ == "__main__":
    main()
