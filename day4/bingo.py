#!/usr/bin/python3

# Class for Bingo board and numbers

class Board:
    def __init__(self, board, winner):
        self.board = board
        self.winner = winner

    def mark_number(board, number):
        for row in board.board:
            for num in row:
                if num.value == number:
                    num.marked = True

    def check_board(board):
        # Check rows for bingo 
        for row in board.board:
            bingo = [num for num in row if num.marked]
            if len(bingo) == 5:
                board.winner = True

        # Check columns for bingo
        for i in range(5):
            bingo = list()
            for row in board.board:
                bingo.append(row[i])
            bingo = [num for num in bingo if num.marked]
            if len(bingo) == 5:
                board.winner = True

        return board.winner

    def sum_unmarked(board):
        total = 0
        for row in board.board:
            for num in row:
                if num.marked == False:
                    total += int(num.value)

        return total

class Number:
    def __init__(self, value, marked=False):
        self.value = value
        self.marked = marked
