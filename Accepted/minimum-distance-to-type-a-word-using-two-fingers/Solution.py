class Solution:
    def minimumDistance(self, word: str) -> int:

        def pos(c):
            x = c // 6
            y = c % 6
            return x, y

        def dist(a, b):
            # 26 = unused/free finger
            if a == 26 or b == 26:
                return 0

            x1, y1 = pos(a)
            x2, y2 = pos(b)

            return abs(x1 - x2) + abs(y1 - y2)

        dp = [float('inf')] * 27
        dp[26] = 0

        prev = ord(word[0]) - ord('A')

        for ch in word[1:]:
            cur = ord(ch) - ord('A')

            new_dp = [float('inf')] * 27

            for free in range(27):

                # Finger on prev moves to cur
                new_dp[free] = min(
                    new_dp[free],
                    dp[free] + dist(prev, cur)
                )

                # Free finger moves to cur
                new_dp[prev] = min(
                    new_dp[prev],
                    dp[free] + dist(free, cur)
                )

            dp = new_dp
            prev = cur

        return min(dp)