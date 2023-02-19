import random
from pprint import pprint


def candy_crush(board, n, k):
    result = True
    for r in range(n):
        for c in range(n-k):
            if all(board[r][c] == board[r][c+i] and board[r][c] != 0 for i in range(1, k)):
                for x in range(k):
                    board[r][c + x] = -board[r][c + x]
                result = False

    for c in range(n):
        for r in range(n-k+1):
            if all(board[r][c] == board[r+i][c] and board[r][c] != 0 for i in range(1, k)):
                for x in range(k):
                    board[r+x][c] = -board[r+x][c]
                result = False

    if not result:
        for c in range(n):
            idx = n - 1
            for r in range(n - 1, -1, -1):
                if board[r][c] > 0:
                    board[idx][c] = board[r][c]
                    idx -= 1

            for r in range(idx, -1, -1):
                board[r][c] = 0

    return board if result else candy_crush(board, n, k)


n_matrix = int(input("Enter the number of matrix: "))
k_kof = int(input("Enter the number of sequences: "))
# game_board = [[random.randint(1, n-1) for _ in range(n)] for _ in range(n)]
game_board = [[1, 2, 3, 4, 5, 1],
              [5, 1, 1, 2, 1, 3],
              [3, 2, 4, 3, 4, 2],
              [2, 4, 4, 1, 4, 2],
              [1, 3, 1, 1, 1, 1],
              [2, 2, 4, 5, 2, 2]]
pprint(game_board)
print()
pprint(candy_crush(game_board, n_matrix, k_kof))
