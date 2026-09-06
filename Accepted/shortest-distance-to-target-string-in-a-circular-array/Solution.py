class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                distance = abs(i - startIndex)
                distance = min(distance, n - distance)

                ans = min(ans, distance)

        return -1 if ans == float('inf') else ans