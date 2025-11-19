class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bank = {}

        for i in range(0, len(nums)):            

            if target - nums[i] in bank:
                return [bank[target - nums[i]], i]
            
            bank[nums[i]] = i
