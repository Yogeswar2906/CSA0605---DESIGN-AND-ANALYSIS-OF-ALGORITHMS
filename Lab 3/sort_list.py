def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Test Case 1
arr = []
print("Input:", arr)
print("Output:", bubble_sort(arr))

# Test Case 2
arr = [1]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))

# Test Case 3
arr = [7, 7, 7, 7]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))

# Test Case 4
arr = [-5, -1, -3, -2, -4]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))