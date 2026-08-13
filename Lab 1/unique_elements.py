def unique_elements(arr):
    unique = []

    for num in arr:
        if num not in unique:
            unique.append(num)

    return unique

# Test Case 1
arr = [3, 7, 3, 5, 2, 5, 9, 2]
print("Input:", arr)
print("Output:", unique_elements(arr))

# Test Case 2
arr = [-1, 2, -1, 3, 2, -2]
print("\nInput:", arr)
print("Output:", unique_elements(arr))

# Test Case 3
arr = [1000000, 999999, 1000000]
print("\nInput:", arr)
print("Output:", unique_elements(arr))

print("\nSpace Complexity: O(n)")