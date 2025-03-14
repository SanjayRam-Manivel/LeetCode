class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i , num in enumerate(nums):
            solution = target - num

            if solution in num_map:
                return [num_map[solution],i]
            num_map[num] = i

        return []
        