def sort_and_find_max(arr):
    if len(arr) == 0:
        return "List is empty"

    arr.sort()
    return arr[-1]

# Test Case 1
arr = []
print("Input:", arr)
print("Output:", sort_and_find_max(arr))

# Test Case 2
arr = [5]
print("\nInput:", arr)
print("Output:", sort_and_find_max(arr))

# Test Case 3
arr = [3, 3, 3, 3, 3]
print("\nInput:", arr)
print("Output:", sort_and_find_max(arr))