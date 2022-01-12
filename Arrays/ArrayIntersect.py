#Problem
# Given two integer arrays nums1 and nums2,  return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

#Atempt 1: Brute force O(N²)
def intersect(nums1, nums2):
    intersection = []
    for number in nums1:
        for number2 in nums2:
            if number == number2:
                intersection.append(number)
                nums2.remove(number)
                break
    return intersection

# Atempt 2: dictionaries
def intersect_by_dictionary(nums1, nums2):
    ocurrence    = {}
    intersection = []
    #Build a dictionary such as {num: count}
    for number in nums1:
        ocurrence[number] = ocurrence.get(number,0) + 1
    for number in nums2:
        if number in ocurrence and ocurrence[number] > 0:
            intersection.append(number)
            #Diminish ocurrences in dictonary, only add
            ocurrence[number]-=1
    return intersection
nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersect_by_dictionary(nums1,nums2))
