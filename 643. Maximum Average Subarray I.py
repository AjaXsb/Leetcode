class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = float('-inf')
        currentSum = 0
        i = 0
        for j in range(len(nums)):
            currentSum += nums[j]
            if j >= k - 1:
                maxSum = max(maxSum, currentSum)
                currentSum -= nums[i]
                i += 1

        return maxSum / k

            
