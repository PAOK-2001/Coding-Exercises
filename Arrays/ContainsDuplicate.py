#Problem
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
def containsDuplicate(nums):
    nums.sort()
    j = 0
    for i in range(1,len(nums)):
        if nums[j] ==nums[i]:
            return True
        j+=1
    return False
 
test = [1,1,2,2,3,4,4]
print(containsDuplicate(test))

