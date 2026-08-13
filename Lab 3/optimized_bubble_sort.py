def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

# Test Case 1
arr = [64, 25, 12, 22, 11]
print("Input:", arr)
print("Output:", bubble_sort(arr))

# Test Case 2
arr = [29, 10, 14, 37, 13]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))

# Test Case 3
arr = [3, 5, 2, 1, 4]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))

# Test Case 4
arr = [1, 2, 3, 4, 5]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))

# Test Case 5
arr = [5, 4, 3, 2, 1]
print("\nInput:", arr)
print("Output:", bubble_sort(arr))