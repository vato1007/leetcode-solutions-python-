from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        last = defaultdict(lambda: [-1, -1])
        ans = float("inf")

        for i, x in enumerate(nums):
            a, b = last[x]

            if a != -1:
                ans = min(ans, 2 * (i - a))

            last[x] = [b, i]

        return -1 if ans == float("inf") else ans