from heapq import merge

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        res = []
        res = list(merge(nums1, nums2))

        length = len(res)
        if (length % 2 == 0):
            idx1 = (length / 2) - 1
            idx2 = idx1 + 1

            return (float(res[idx1] + res[idx2]) / 2)
        
        else:
            idx = (length / 2)

            return float(res[idx])
