# coding: utf-8


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0  # 记录当前无重复的最长子串
        left = -1  # 记录最长子串 最左 的前一个位置 的坐标
        position = dict()  # 记录每个字符 最近一次出现 的坐标
        for i in xrange(0, len(s), 1):
            if s[i] in position and position[s[i]] > left:
                left = position[s[i]]
            position[s[i]] = i
            res = max(res, i-left)
        return res


if __name__ == '__main__':
    s = 'abcabcbb'
    res = Solution().lengthOfLongestSubstring(s)
    print res
