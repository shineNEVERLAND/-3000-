class Solution(object):

    def twoSum(self, nums, target):
        if nums == [] or target is None:
            return _, _

        dic = dict()
        for i, value in enumerate(nums):
            difference = target - value
            pos = dic.get(difference)
            if pos is None:
                dic[value] = i
            else:
                return nums[i], nums[pos]

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == [] or len(nums) < 3:
            return []

        result = []
        for i, value in enumerate(nums):
            difference = 0 - value
            v_a, v_b = self.twoSum(nums[i+1: len(nums)], difference)
            result.append([nums[i], v_a, v_b])

        return result
