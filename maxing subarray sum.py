def maxSubArray(nums):
    curr = nums[0]
    max_val = nums[0]

    for num in nums[1:]:
        curr = max(num, curr + num)
        max_val = max(max_val, curr)

    return max_val


nums = [5]
print(maxSubArray(nums))
