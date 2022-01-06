#include<bits/stdc++.h>
using namespace std;
//Problem:

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
// However, you can buy it then immediately sell it on the same day.
// Find and return the maximum profit you can achieve.


class Solution {
// Approach: scan the price array looking for consecutive increments, resulting in  profit add up all profit that can be made
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        for (int current = 1; current < prices.size(); current++){
            int currentPrice = prices[current];
            int prevPrice = prices[current-1];
            if(currentPrice > prevPrice){
                maxProfit += currentPrice -prevPrice;
            }
        }
        return maxProfit;
    }
};

int main(){
    vector<int> test = {7,1,5,3,6,4};
    Solution s1;

    cout<<s1.maxProfit(test)<<endl;
}