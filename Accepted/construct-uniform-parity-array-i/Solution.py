class Solution:
    def uniformArray(self, nums1):
        odd = sum(x % 2 for x in nums1)
        even = len(nums1) - odd

        # Already all odd or all even
        if odd == 0 or even == 0:
            return True

        # If there is at least one odd number,
        # we can make every even number odd by
        # subtracting an odd number.
        return True