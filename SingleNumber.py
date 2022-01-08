def findSingle(nums):
    #Sort the array so the duplicate numbers arre consecutibe
    nums.sort()
    #Iterate through nums with a step of 2
    current = 0
    for i in range(0,len(nums),2):
        # Compare current and next position, if different return nums[i]
        if i+1 >=len(nums):
            return nums[i]
        elif(nums[i]!= nums[i+1]):
            return nums[i]
test = [1,1,2,2,4,3,3]
print(findSingle(test))
