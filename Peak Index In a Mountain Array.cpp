/* https://leetcode.com/problems/peak-index-in-a-mountain-array/ */

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int left=0,right=1;

  
        while (A[left] < A[right])
        {
            left++;
            right++;
        }
        return left;
    }   
};
            
       
