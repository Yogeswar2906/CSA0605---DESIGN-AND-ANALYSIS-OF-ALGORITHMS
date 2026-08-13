def find_peak(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Test Case 1
nums = [1, 2, 3, 1]
print("Input:", nums)
index = find_peak(nums)
print("Output:", index)

# Test Case 2
nums = [1, 2, 1, 3, 5, 6, 4]
print("\nInput:", nums)
index = find_peak(nums)
print("Output:", index)