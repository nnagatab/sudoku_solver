# sudoku solver prompt found online

b = [[0, 4, 0, 7, 0, 0, 1, 3, 0],
     [0, 0, 2, 0, 0, 0, 6, 0, 0],
     [0, 0, 0, 4, 2, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 2, 0, 0, 3],
     [2, 3, 1, 0, 7, 0, 0, 8, 0],
     [4, 0, 0, 3, 1, 0, 0, 0, 0],
     [0, 7, 0, 0, 0, 8, 0, 0, 0],
     [0, 0, 6, 0, 3, 0, 0, 0, 4],
     [8, 9, 0, 0, 5, 0, 0, 0, 6]]


def solve(board):   # uses recurision and a backtracking method to solve the sudoku board
    for row in board:
        for i in range(9):
            if row[i] == 0:
                for num in range(1,10):
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


def print_board():
    for i in b:
        print(i)


solve(b)
print_board()
