# include<bits/stdc++.h>

using namespace std;

// Problem

// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
// The relative order of the elements should be kept the same.
// Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
// More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
// It does not matter what you leave beyond the first k elements.

// Return k after placing the final result in the first k slots of nums.

// Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // The solution has a slow and fast counter. The slow counter only advances when it is different of the fast counter.
        int slow = 0;
        int returnIndex;
         if(nums.size()== 0){
            return 0;
        }
        for (int fast = 0; fast < nums.size(); fast++){
            // If slow an fast counter are different advance the slow counter and update array value to the las position traverse by fast counter.
            if(nums[slow]!= nums[fast]){
                slow++;
                nums[slow] = nums[fast];
            }
            returnIndex = slow;
        }

        return returnIndex;
        
    }

    void printVector(vector<int> nums, int limit){
        for (int i = 0; i <= limit; i++){
            cout<<nums[i]<<endl;
        }
    }
};

int main(){
    vector<int> test = {0,0,0,1,2,3,4,4,5,6,6,7,8,9,10};
    Solution s1;
    int limit = s1.removeDuplicates(test);
    cout<< limit<<endl;
    s1.printVector(test, limit);

}