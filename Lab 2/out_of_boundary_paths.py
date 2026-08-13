def find_paths(m, n, N, i, j):
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    count = 0

    for step in range(N):
        new_dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if dp[row][col] > 0:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_row = row + dr
                        new_col = col + dc

                        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                            count += dp[row][col]
                        else:
                            new_dp[new_row][new_col] += dp[row][col]

        dp = new_dp

    return count

# Test Case 1
print("Input: m=2, n=2, N=2, i=0, j=0")
print("Output:", find_paths(2, 2, 2, 0, 0))

# Test Case 2
print("\nInput: m=1, n=3, N=3, i=0, j=1")
print("Output:", find_paths(1, 3, 3, 0, 1))