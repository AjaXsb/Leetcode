class Solution {
public:
    int reverse(int x) {
        
        int y;
        int rev=0;
    
        while (x!=0)
        {
            y=x%10;
            x=x/10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && y > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && y < -8)) return 0;
            rev=rev*10+y;
                  
        }
        return rev;
       
    }
};