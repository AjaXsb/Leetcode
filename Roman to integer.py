# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        s = list(s)
        n = 0
        size = len(s)
        j = 0
        rtoi = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(size):

            if j == size or j > size:
                break

            if j != size - 1:
                if rtoi[s[j]] < rtoi[s[j + 1]]:
                    n += rtoi[s[j + 1]] - rtoi[s[j]]
                    j += 2
                    continue

                else:
                    n += rtoi[s[j]]
                    j += 1

            else:
                n += rtoi[s[j]]
                j += 1
                
        return n