def rob_houses(nums):
    if len(nums) == 1:
        return nums[0]

    def rob(arr):
        prev1 = 0
        prev2 = 0

        for money in arr:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1

    return max(rob(nums[:-1]), rob(nums[1:]))

# Test Case 1
nums = [2, 3, 2]
print("Input:", nums)
print("Output: The maximum money you can rob without alerting the police is",
      rob_houses(nums))

# Test Case 2
nums = [1, 2, 3, 1]
print("\nInput:", nums)
print("Output: The maximum money you can rob without alerting the police is",
      rob_houses(nums))