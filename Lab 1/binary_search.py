def binary_search(arr, key):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Test Case 1
arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 10
print("Input:", arr)
position = binary_search(arr, key)
if position != -1:
    print("Output: Element", key, "is found at position", position)
else:
    print("Output: Element", key, "is not found")

# Test Case 2
arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 100
print("\nInput:", arr)
position = binary_search(arr, key)
if position != -1:
    print("Output: Element", key, "is found at position", position)
else:
    print("Output: Element", key, "is not found")

print("\nTime Complexity: O(log n)")