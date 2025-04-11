class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        childCounter = 0
        parentCounter = 0

        while parentCounter < len(t):

            if t[parentCounter] == s[childCounter]:
                childCounter += 1

                if childCounter == len(s):
                    return True

            parentCounter += 1    
        return False