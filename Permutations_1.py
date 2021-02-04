# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = 0
        r = len(nums) - 1
        final = []
        fact = math.factorial(int(r + 1))
        
        if fact == 1:
            final.append(list(nums))
            return final

        def perm(num_list, l , r, final, fact):

            if l == r:
                final.append(list(num_list))

            else:
                for i in range(l, r + 1):

                    num_list[l], num_list[i] = num_list[i], num_list[l]
                    perm(num_list, l + 1, r, final, fact)
                    num_list[l], num_list[i] = num_list[i], num_list[l]

                    if len(final) == fact:
                        return final


        return perm(nums, l, r, final, fact)