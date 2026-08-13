def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

# Test Case 1
arr = [1, 2, 3, 4, 5]
print("Input:", arr)
print("Output:", find_largest(arr))

# Test Case 2
arr = [7, 7, 7, 7, 7]
print("\nInput:", arr)
print("Output:", find_largest(arr))

# Test Case 3
arr = [-10, 2, 3, -4, 5]
print("\nInput:", arr)
print("Output:", find_largest(arr))