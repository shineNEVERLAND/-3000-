class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = []
        middle = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or middle:
            tmp = 0
            if i >= 0:
                tmp += int(a[i])
                i -= 1
            if j >= 0:
                tmp += int(b[j])
                j -= 1
            tmp += middle
            result.append(str(tmp % 2))
            middle = tmp / 2

        s = result[::-1]
        return ''.join(s)