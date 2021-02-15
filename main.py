

global board
board = [[0, 4, 0, 7, 0, 0, 1, 3, 0],
         [0, 0, 2, 0, 0, 0, 6, 0, 0],
         [0, 0, 0, 4, 2, 0, 0, 0, 0],
         [6, 0, 0, 0, 0, 2, 0, 0, 3],
         [2, 3, 1, 0, 7, 0, 0, 8, 0],
         [4, 0, 0, 3, 1, 0, 0, 0, 0],
         [0, 7, 0, 0, 0, 8, 0, 0, 0],
         [0, 0, 6, 0, 3, 0, 0, 0, 4],
         [8, 9, 0, 0, 5, 0, 0, 0, 6]]


def solve():
    for i in board:
        for x in i:
            if x == 0:
                for num in range(1,10):
                    if is_valid(board.index(i), i.index(x), num):
                        i[x] = num
                        x = solve()
                        if x:
                            return True
                        else:
                            i[x] = 0
                return False
    return True


def is_valid(row, col, num):
    # row - row%3 (gives row of top left of square)
    # col - col%3 (gives col of top left of square)

    # get top-left corner of 3x3
    boxRow = row - row % 3
    boxCol = col - col % 3

    # check row
    for i in board[row]:
        if i == num:
            return False

    # check col
    for x in board:
        if num == x[col]:
            return False

    # check 3x3
    for y in range(0, 3):
        for z in range(0, 3):
            if num == board[boxRow + y][boxCol + z]:
                return False

    # return true if none of the cases returns False
    return True


def print_board():
    for i in board:
        print(str(i))


def main():
    solve()
    print_board()


main()
