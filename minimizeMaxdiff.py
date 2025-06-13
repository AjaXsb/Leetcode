def minimizeMax(self, nums, p):
    if p == 0:
        return 0
    
    nums.sort()

    left, right = 0, nums[-1] - nums[0]

    while left < right:
        mid = left + (right - left) // 2

        if can_form_pairs(nums, p, mid):
            right = mid

        else:
            left = mid + 1

    return left

def can_form_pairs(self, nums, p, diff):
    count = 0
    i = 0

    while i < len(nums) - 1:

        if nums[i + 1] - nums[i] <= diff:
            count += 1
            i += 2

        else:
            i += 1

    return count <= p

# TIME COMPLEXITY
# Sorting - O(n log n)
# Binary search - O(log diff)
# con form pairs - O(n)
# O(n log n) + O(log diff) 

# SPACE COMPLEXITY
# depends on whether sort uses extra space O(n) or not O(1)