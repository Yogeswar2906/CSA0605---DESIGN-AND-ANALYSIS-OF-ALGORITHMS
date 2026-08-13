def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

# Test Case 1
nums = [5, 2, 3, 1]
print("Input:", nums)
print("Output:", merge_sort(nums))

# Test Case 2
nums = [5, 1, 1, 2, 0, 0]
print("\nInput:", nums)
print("Output:", merge_sort(nums))

print("\nTime Complexity: O(n log n)")
print("Space Complexity: O(n)")