def sum_counts(nums):
    total = 0

    for i in range(len(nums)):
        distinct = set()
        for j in range(i, len(nums)):
            distinct.add(nums[j])
            count = len(distinct)
            total += count * count

    return total

# Test Case 1
nums = [1, 2, 1]
print("Input:", nums)
print("Output:", sum_counts(nums))

# Test Case 2
nums = [1, 1]
print("\nInput:", nums)
print("Output:", sum_counts(nums))