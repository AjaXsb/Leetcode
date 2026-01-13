class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        smallestSubarray = float(inf)
        i = 0
        calculatedSum = 0
        for j in range(len(nums)):
            calculatedSum += nums[j]
            while calculatedSum >= target:
                smallestSubarray = min(smallestSubarray, j - i + 1)
                calculatedSum -= nums[i]
                i += 1

        return smallestSubarray if smallestSubarray != float(inf) else 0

        