class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Start with the only possible move when 2 stones remain
        ans = prefix[n - 1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans