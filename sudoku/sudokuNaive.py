#! /usr/bin/python3

import sys

inp = open(sys.argv[1], 'r')
out = open(sys.argv[2], 'w')
name_of_board = sys.argv[3]
backtracks = 0
board_state = []

# size stuff
SIZE = 9
board = []

# parse stuff
def getBoard():
    board = []
    lines = [x.strip() for x in inp.readlines()]
    for i in range(1, 10):
        row = lines[lines.index(name_of_board) + i].strip().split(",")
        for i in range(9):
            if row[i] == '_':
                row[i] = 0
            else:
                row[i] = int(row[i])
        board.append(row)
    return board

board = getBoard()

# base case if the board is not solved yet
def is_solved(row, col):
    isSolved = True
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            # if cell isnt assigned
            if board[i][j] == 0:
                row = i
                col = j
                isSolved = False
                a = [row, col, isSolved]
                return a
    a = [-1, -1, isSolved]
    return a

# check if n is valid in row col and box
def is_safe(n, r, c):
    # check if n is valid in row
    for i in range(0, SIZE):
        # there is a cell with same value
        if board[r][i] == n:
            return False

    # check if n is valid in column
    for i in range(0, SIZE):
        # there is a cell with same value
        if board[i][c] == n:
            return False

    # check if n is valid in box
    # width/height
    row_start, col_start = (r // 3) * 3, (c // 3) * 3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if board[i][j] == n:
                return False
    return True

def valid_list(r, c):
    ret = []
    for i in range(0, 10):
        if is_safe(i, r, c):
            ret.append(i)
    return ret
    
def get_smallest():
    temp = is_solved(0, 0)
    ret = valid_list(temp[0], temp[1])
    print(board)
    for row in range(0, 10):
        for col in range(0, 10):
            if board[row][col] == 0:
                if len(valid_list(row, col)) <= len(ret): ret = valid_list(row, col) 
    return ret

print(get_smallest())

# smarter algo 1: fill in cells we are CERTAIN of
for row in range(0, 10):
    for col in range(0, 10):
        if board[row][col] == 0:
            temp = valid_list(row, col)
            # print(temp)
            if len(temp) == 1:
                board[row][col] = temp[0]

# recursive solver
def solve():
    row, col = 0, 0
    global backtracks
    # if all cells are assigned then the sudoku is already solved
    a = is_solved(row, col)
    if a[2]: return True
    row = a[0]
    col = a[1]

    lis = valid_list(row, col)
    for i in lis:
        # check if i is a valid cell
        board[row][col] = i

        # backtracking
        if solve():
            return True
        # reassign the cell
        backtracks += 1
        board[row][col] = 0

    return False

# use least guesses
def solve2():
    row, col = 0, 0
    # if all cells are assigned then the sudoku is already solved
    a = is_solved(row, col)
    if a[2]: return True
    row = a[0]
    col = a[1]
    global backtracks
    global board
    global board_state

    lis = valid_list(row, col)
    for i in lis:
        board_state.append(board)
        # check if i is a valid cell
        board[row][col] = i

        # smarter algo 1: fill in cells we are CERTAIN of
        for rows in range(0, 9):
            for cols in range(0, 9):
                if board[rows][cols] == 0:
                    temp = valid_list(rows, cols)
                    if len(temp) == 1:
                        board[rows][cols] = temp[0]
        # backtracking
        if solve2():
            return True
        # reassign the cell
        backtracks += 1
        board[row][col] = 0
        print(board_state)
        board = board_state[len(board_state) - 1]
    return False

def write():
    solve()
    print(backtracks)
    # name_of_solved_board = name_of_board.replace('unsolved', 'solved') + '\n'
    # out.write(name_of_solved_board)
    for i in range(9):
        out.write(','.join([str(x) for x in board[i]]) + '\n')

write()