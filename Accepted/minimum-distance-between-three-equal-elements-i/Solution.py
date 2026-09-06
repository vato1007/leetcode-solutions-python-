from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        positions = defaultdict(list)
        ans = float("inf")

        for i, x in enumerate(nums):
            positions[x].append(i)

            if len(positions[x]) >= 3:
                a, b, c = positions[x][-3:]
                ans = min(ans, 2 * (c - a))

        return -1 if ans == float("inf") else ans