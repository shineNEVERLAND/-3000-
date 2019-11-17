# coding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        goal = dict()
        for i in xrange(0, len(nums), 1):
            aim = target - nums[i]
            value = goal.get(aim, None)
            if value is None:
                goal[nums[i]] = i
            else:
                return [i, value]


if __name__ == '__main__':
    s = [2,7,11,15]
    target = 9
    res = Solution().twoSum(s, target)
    print res