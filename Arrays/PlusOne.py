# Problem
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits

def plusOne(digits):
    carryOut = False
    for i in range(len(digits)-1,-1,-1):
        if digits[i] != 9 or (carryOut and digits[i]!=9):
            digits[i]+=1
            carryOut = False
            break;
   
        else:
            digits[i]= 0 
            carryOut = True
       
    if carryOut:
        digits.insert(0,1)
    return digits
            
test = [9,9]
print(plusOne(test))
