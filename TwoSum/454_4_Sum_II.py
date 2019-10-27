class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if len(A) != len(B) != len(C) != len(D):
            return 0
        res = 0
        dicAB = dict()
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                pos = dicAB.get(A[i] + B[j])
                if pos is None:
                    dicAB.update({A[i] + B[j]: 1})
                else:
                    dicAB[A[i] + B[j]] = dicAB[A[i] + B[j]] + 1

        for i in range(0, len(C)):
            for j in range(0, len(D)):
                target = 0 - C[i] - D[j]
                pos = dicAB.get(target, None)
                if pos is not None:
                    res = res + pos

        return res
