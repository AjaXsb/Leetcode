class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Initial Thought Process

        #[1,1,1,2,2,3]
        #
        #start at 
        #i = 0
        #j = 1
#
        #double = false
#
        #if double true and same val then j moves
        #if double true and different val then i += 1 and a[i] = a[j] and j += 1 and double = false
        #if double false and same val then i += 1 and j += 1 and double = true
        #if double false and different val then i += 1 and a[i] = a[j] 

        if not nums:
            return 0

        i = 0  # Pointer for placing the next valid element
        count = 1  # Tracks occurrences of the current number

        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += 1
                if count <= 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                count = 1
                i += 1
                nums[i] = nums[j]

        return i + 1

        