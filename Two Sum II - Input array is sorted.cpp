class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int x=0,y=size(numbers)-1,r;
        
        while (numbers[x] + numbers[y] != target)
        {
            r=numbers[x]+numbers[y];
            
            if (r>target)
            {
                y--;
            }
            else 
            {
                x++;
            }
        }
        x++;
        y++;
        vector<int> ans;
        ans.push_back(x);
        ans.push_back(y);
        
        return ans;
        
    }
};