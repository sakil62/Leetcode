class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2   # partition index for nums1
            j = half - i            # partition index for nums2

            # Boundaries for nums1
            maxLeft1 = float("-inf") if i == 0 else nums1[i - 1]
            minRight1 = float("inf") if i == m else nums1[i]

            # Boundaries for nums2
            maxLeft2 = float("-inf") if j == 0 else nums2[j - 1]
            minRight2 = float("inf") if j == n else nums2[j]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd length → take max from left
                if total % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even length → average of two middles
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0

            # Move binary search boundaries
            elif maxLeft1 > minRight2:
                high = i - 1  # too far right in nums1
            else:
                low = i + 1   # too far left in nums1
