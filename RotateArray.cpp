#include<bits/stdc++.h>

using namespace std;

// Problem
// Given an array, rotate the array to the right by k steps, where k is non-negative.


// First aproach: get last item and move all elements in array over one place.
// Notes: works on 34 test cases but fails bc of time limit exceded.
// Time Complexity O(N²)
// Space Complexity O(1)
class Solution1 {
public:
    void rotate(vector<int>& nums, int k) {
        if(nums.size()==0){
            return;
        }
        for (int i = 0; i < k; i++){
            int last = nums[nums.size()-1];
            int prev = nums[0];
            for (int j = 1; j < nums.size(); j++){
                int temp = nums[j];
                nums[j]=prev;
                prev = temp;
            }
            nums[0] = last;
        }
        
    }
};

class Solution2{
public:
    void rotate(vector<int>& nums, int k) {
        
    }
};

int main(){
    vector <int> test = {1,2,3,4,5,6,7};
    Solution1 s1;
    s1.rotate(test, 3);

    for (int i = 0; i < test.size(); i++){
        cout<<test[i]<<" ";
    }
    cout<<endl;
}