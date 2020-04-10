import matplotlib.pyplot as plt
import sys

invalid_options = [(0,0), (0,1), (0,5), (0,6), (1,0), (1,1), (1,5), (1,6), (5,0), (5,1), (5,5), (5,6), (6,0), (6,1), (6,5), (6,6)]

path_already_taken = {}

def isValid(x, y):
    if x >= 0 and y >= 0 and x <= 6 and y <= 6 and (x,y) not in invalid_options:
        return True
    return False

def print_board(board):
    x = []
    y = []
    for i in range(7):
        for j in range(7):
            if board[i][j] == 1:
                x.append(i)
                y.append(j)
    plt.scatter(x, y)
    plt.show()


def init_board():
    board = [[1]*7 for i in range(7)]
    for x in invalid_options:
        board[x[0]][x[1]] = 0
    board[3][3] = 0
    return board

def board_solved(board):
    count = 0
    for i in range(7):
        for j in range(7):
            count = count + board[i][j]
    if count == 1 and board[3][3] == 1:
        return True
    return False

def solve(board, steps):
    if board_solved(board):
        print("steps are : " + str(steps))
        print_board(board)
        sys.exit()

    if len(steps) == 31:
        # need to backtrack
        return
    for i in range(7):
        for j in range(7):
            if not isValid(i,j):
                continue
            if board[i][j] == 0:
                continue

            if isValid(i-1,j) and board[i-1][j] == 1 and isValid(i-2,j) and board[i-2][j] == 0 and (str(board)+str(((i,j),(i-2,j))) not in path_already_taken):
                new_steps = steps[:]
                new_steps.append(((i,j),(i-2,j)))
                new_board = [row[:] for row in board]
                new_board[i][j] = 0
                new_board[i-1][j] = 0
                new_board[i-2][j] = 1
                solve(new_board, new_steps)
                path_already_taken[str(board)+str(((i,j),(i-2,j)))] = True
            if isValid(i+1,j) and board[i+1][j] == 1 and isValid(i+2,j) and board[i+2][j] == 0 and (str(board)+str(((i,j),(i+2,j))) not in path_already_taken):
                new_steps = steps[:]
                new_steps.append(((i,j),(i+2,j)))
                new_board = [row[:] for row in board]
                new_board[i][j] = 0
                new_board[i+1][j] = 0
                new_board[i+2][j] = 1
                solve(new_board, new_steps)
                path_already_taken[str(board)+str(((i,j),(i+2,j)))] = True
            if isValid(i,j-1) and board[i][j-1] == 1 and isValid(i,j-2) and board[i][j-2] == 0 and (str(board)+str(((i,j),(i-2,j))) not in path_already_taken):
                new_steps = steps[:]
                new_steps.append(((i,j),(i-2,j)))
                new_board = [row[:] for row in board]
                new_board[i][j] = 0
                new_board[i][j-1] = 0
                new_board[i][j-2] = 1
                solve(new_board, new_steps)
                path_already_taken[str(board)+str(((i,j),(i-2,j)))] = True
            if isValid(i,j+1) and board[i][j+1] == 1 and isValid(i,j+2) and board[i][j+2] == 0 and (str(board)+str(((i,j),(i,j+2))) not in path_already_taken):
                new_steps = steps[:]
                new_steps.append(((i,j),(i,j+2)))
                new_board = [row[:] for row in board]
                new_board[i][j] = 0
                new_board[i][j+1] = 0
                new_board[i][j+2] = 1
                solve(new_board, new_steps)
                path_already_taken[str(board)+str(((i,j),(i,j+2)))] = True


def main():
    board = init_board()
    print_board(board)
    steps = []
    solve(board, steps)
    print("No solution !!!")

if __name__ == "__main__":
    main()
