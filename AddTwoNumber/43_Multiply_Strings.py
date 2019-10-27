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
                carry = (res[i + j + 1] + tmp) // 10
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10
            res[i] += carry
        s = ''.join(map(str, res))
        return "0" if not s.lstrip("0") else s.lstrip("0")
