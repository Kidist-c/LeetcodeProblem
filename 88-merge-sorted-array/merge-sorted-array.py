class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2, and the end of nums1
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        