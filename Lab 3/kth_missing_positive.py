def find_kth_positive(arr, k):
    current = 1
    index = 0

    while k > 0:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            k -= 1
            if k == 0:
                return current
        current += 1

# Test Case 1
arr = [2, 3, 4, 7, 11]
k = 5
print("Input:")
print("arr =", arr)
print("k =", k)
print("Output:", find_kth_positive(arr, k))

# Test Case 2
arr = [1, 2, 3, 4]
k = 2
print("\nInput:")
print("arr =", arr)
print("k =", k)
print("Output:", find_kth_positive(arr, k))