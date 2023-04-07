nums = [1, 2, 3, 4, 5, 6]

print(nums)


def change_nums(nums):
    nums[len(nums) - 1] = 99
    nums = []
    return nums


print(change_nums(nums))
print(nums)
