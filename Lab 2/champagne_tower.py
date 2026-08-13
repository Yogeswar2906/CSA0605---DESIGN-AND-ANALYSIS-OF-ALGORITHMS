def champagne_tower(poured, query_row, query_glass):
    glasses = [[0.0] * (i + 1) for i in range(query_row + 1)]
    glasses[0][0] = poured

    for i in range(query_row):
        for j in range(i + 1):
            excess = (glasses[i][j] - 1.0) / 2.0

            if excess > 0:
                glasses[i + 1][j] += excess
                glasses[i + 1][j + 1] += excess

    return min(1.0, glasses[query_row][query_glass])

# Test Case 1
poured = 1
query_row = 1
query_glass = 1
print("Input: poured =", poured, ", query_row =", query_row, ", query_glass =", query_glass)
print("Output: {:.5f}".format(champagne_tower(poured, query_row, query_glass)))

# Test Case 2
poured = 2
query_row = 1
query_glass = 1
print("\nInput: poured =", poured, ", query_row =", query_row, ", query_glass =", query_glass)
print("Output: {:.5f}".format(champagne_tower(poured, query_row, query_glass)))