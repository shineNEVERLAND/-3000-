class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        B = []
        while K > 0:
            tmp = K % 10
            B.append(tmp)
            K /= 10
        C = B[::-1]

        i = len(A) - 1
        j = len(C) - 1
        result = []
        middle = 0
        while i >= 0 or j >= 0 or middle:
            tmp = 0
            if i >= 0:
                tmp += A[i]
                i -= 1
            if j >= 0:
                tmp += C[j]
                j -= 1
            tmp += middle
            result.append(tmp % 10)
            middle = tmp / 10
        return result[::-1]

