#Problem

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    ordered   = nums.copy()
    ordered.sort()
    nums_hash = {}
    lower = 0 
    upper = len(nums)

    for i in range(len(nums)):
        nums_hash[nums[i]]= i
    
    print(nums_hash)

    for i in range(len(nums)):
        if ordered[i] >= target:
            upper = i

    for j in range(1,upper):
        test = ordered[lower] + ordered[j]
        if test == target:
            return [nums_hash[ordered[lower]], nums_hash[ordered[j]]]
    
nums = [1,3,3,2,4]
target = 6
print(twoSum(nums,target))