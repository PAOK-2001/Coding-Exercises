#Problem
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

#Two pointer:
    # A pointer that always moves
    # If the pointer value is different from zero refresh lastZero value and move second pointer up   
def moveZeroes(nums):
    iterator = 0
    lastZero = 0
    while(iterator <= (len(nums)-1)):
        if nums[iterator] != 0:
            temp = nums[iterator]
            nums[iterator] = 0
            nums[lastZero] = temp
            lastZero +=1
        iterator+=1
    print("Iterations", iterator)
nums = [1,0,2,0,0,3]
moveZeroes(nums)
print("Length", len(nums))
print(nums)

    












