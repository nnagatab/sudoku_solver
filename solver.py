# sudoku solver prompt found online
import csv
import random


def solve(board):  # uses recurision and a backtracking method to solve the sudoku board
    for row in board:
        for i in range(9):
            if row[i] == 0:
                for num in range(1, 10):
                    if is_valid(board, board.index(row), i, num):
                        row[i] = num
                        if solve(board):
                            return True
                        else:
                            row[i] = 0
                return False
    return True


def is_valid(bo, row, col, num):
    # row - row%3 (gives row of top left of square)
    # col - col%3 (gives col of top left of square)

    # get top-left corner of 3x3
    boxRow = row - row % 3
    boxCol = col - col % 3

    # check row
    for i in range(9):
        if bo[row][i] == num:
            return False

    # check col
    for x in range(9):
        if bo[x][col] == num:
            return False

    # check 3x3
    for y in range(boxRow, boxRow + 3):
        for z in range(boxCol, boxCol + 3):
            if num == bo[y][z]:
                return False
    # return true if none of the cases returns False
    return True


def print_board(board):
    for i in board:
        print(i)


def generate_board():   # returns random sudoku board out of 1 million
    with open("sudoku.csv", "r") as sudoku_files:
        csv_reader = csv.reader(sudoku_files)
        board, solved= random.choice(list(csv_reader))
        grid = [[int(i) for i in board[i:i+9]] for i in range(0,len(board),9)]
        return grid

'''
x = generate_board()
print(x)
print("before")
print_board(x)
print("after")
solve(x)
print_board(x)
x = generate_solved_board()
removeDigits(x)
print("before" + "\n")
print_board(x)
print("\n" + "after")
solve(x)
print_board(x)
'''
