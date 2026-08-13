def game_of_life(board):
    rows = len(board)
    cols = len(board[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < rows and 0 <= y < cols:
                        if (x != i or y != j) and board[x][y] == 1:
                            live_neighbors += 1

            if board[i][j] == 1 and live_neighbors in [2, 3]:
                result[i][j] = 1
            elif board[i][j] == 0 and live_neighbors == 3:
                result[i][j] = 1

    return result

# Test Case 1
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print("Input:", board)
print("Output:", game_of_life(board))

# Test Case 2
board = [[1,1],[1,0]]
print("\nInput:", board)
print("Output:", game_of_life(board))