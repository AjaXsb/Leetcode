# https://leetcode.com/problems/palindrome-number/

#With converting int to str to list of integer
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        x = list(map(int,str(x)))
        j = len(x) - 1
        n = int(len(x) / 2)
            
        for i in range(n):
            if x[i] != x[j]:
                return False
            
            j -= 1
            
        return True

#Without converting int to str
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        
        rv = 0
        while x > rv:
            rv = x % 10 + rv * 10
            x = int(x /10)
            
        return rv == x or x == int(rv / 10)