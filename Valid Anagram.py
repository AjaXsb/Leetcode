# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        lettersDict = {}

        for i in range(len(s)):
            lettersDict[s[i]] = lettersDict.get(s[i], 0) + 1
            lettersDict[t[i]] = lettersDict.get(t[i], 0) - 1

        return all(value == 0 for value in lettersDict.values())