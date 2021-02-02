/* https://leetcode.com/problems/remove-duplicates-from-sorted-array/ */

class Solution {
public
    int removeDuplicates(vectorint& nums) {
        
        int i=0;
        int j;
        int y=nums.size();
        
        if (nums.size()==0)
        {
            return 0;
        }
        
        for (j=1;j<y;j++)
        {
            if (nums[i] < nums[j])
            {
                i++;
                nums[i]=nums[j];
            }
            
        }
    
        return i+1 ;
        
    }
};