class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        for i in xrange(0, len(nums), 1):
            first = nums[i]
            target = 0 - first
            goal = dict()
            for j in xrange(i+1, len(nums), 1):
                second = nums[j]
                aim = target - second
                if goal.get(aim) is None:
                    goal[nums[j]] = j
                else:
                    _set = {nums[i], aim, nums[j]}
                    _tuple = tuple(_set)
                    result.add(_tuple)
        return list(result)


if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(s)
    print res
