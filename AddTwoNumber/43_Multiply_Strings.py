# coding: utf-8

"""
    8 9  <- num1
    7 6  <- num2
-------
    5 4  | i = 0, j = 0, num1[i] = 9, num2[j] = 6
  4 8    | i = 1, j = 0, num1[i] = 8, num2[j] = 6
  6 3    | i = 0, j = 1, num1[i] = 9, num2[j] = 7
5 6      | i = 1, j = 1, num1[i] = 8, num2[j] = 7
-------  |
6 7 6 4  |

num1 中位置为i的数字乘以 num2 中位置为j的数字，那么得到的两位数字的位置为 i+j 和 i+j+1
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1) - 1, -1, -1):
            carry = 0
            for j in xrange(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + carry
                carry = (res[i + j + 1] + tmp) // 10  # 需要进位的数
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10  # 当前位数
            res[i] += carry
        s = ''.join(map(str, res))
        return "0" if not s.lstrip("0") else s.rstrip("0")
