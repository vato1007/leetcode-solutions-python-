class Solution:
    def uniformArray(self, nums1):
        has_odd = any(x % 2 == 1 for x in nums1)

        if not has_odd:
            return True

        smallest = min(nums1)

        for x in nums1:
            if x % 2 == 0:
                if x - smallest < 1 or (x - smallest) % 2 == 0:
                    return False

        return True