# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                if i == nums.index(a):
                    continue
                else:
                    return [i, nums.index(a)]
                    break
            else:
                continue

print(Solution.twoSum([2,7,11,15],9))