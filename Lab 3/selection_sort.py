def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Test Case 1
arr = [5, 2, 9, 1, 5, 6]
print("Input:", arr)
print("Output:", selection_sort(arr))

# Test Case 2
arr = [10, 8, 6, 4, 2]
print("\nInput:", arr)
print("Output:", selection_sort(arr))

# Test Case 3
arr = [1, 2, 3, 4, 5]
print("\nInput:", arr)
print("Output:", selection_sort(arr))

print("\nTime Complexity: O(n^2)")