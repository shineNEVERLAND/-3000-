import sys


class Solution(object):
    def find(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        cut1 = 0
        cut2 = 0
        cutL = 0
        cutR = len(nums1)
        while (cut1 < len(nums1)):
            cut1 = (cutR - cutL) / 2 + cutL
            cut2 = length / 2 - cut1
            L1 = -sys.maxint - 1 if cut1 == 0 else nums1[cut1 - 1]
            L2 = -sys.maxint - 1 if cut2 == 0 else nums2[cut2 - 1]
            R1 = sys.maxint if cut1 == len(nums1) else nums1[cut1]
            R2 = sys.maxint if cut2 == len(nums2) else nums2[cut2]
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            else:
                if length % 2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return float((L1 + R1) / 2.0)
                else:
                    R1 = min(R1, R2)
                    return R1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and nums2:
            if len(nums2) % 2 == 1:
                return nums2[len(nums2) / 2]
            else:
                mid1 = len(nums2) / 2 - 1
                mid2 = mid1 + 1
                return (nums2[mid1] + nums2[mid2]) / 2.0

        if nums1 and not nums2:
            if len(nums1) % 2 == 1:
                return nums1[len(nums1) / 2]
            else:
                mid1 = len(nums1) / 2 - 1
                mid2 = mid1 + 1
                return (nums1[mid1] + nums1[mid2]) / 2.0

        if len(nums1) > len(nums2):
            return self.find(nums2, nums1)
        else:
            return self.find(nums1, nums2)


if __name__ == '__main__':
    res = Solution().findMedianSortedArrays([], [2,3])
    print res