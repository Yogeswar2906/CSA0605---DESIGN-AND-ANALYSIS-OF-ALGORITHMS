def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Test Case 1
arr = [64, 34, 25, 12, 22, 11, 90]
print("Input:", arr)
print("Sorted Array:", bubble_sort(arr))

# Test Case 2
arr = [5, 1, 4, 2, 8]
print("\nInput:", arr)
print("Sorted Array:", bubble_sort(arr))

# Test Case 3
arr = [3, 3, 2, 1, 5]
print("\nInput:", arr)
print("Sorted Array:", bubble_sort(arr))

print("\nTime Complexity: O(n^2)")