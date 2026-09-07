from collections import defaultdict

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)

        positions = defaultdict(list)

        for i, x in enumerate(nums):
            positions[x].append(i)

        # Answer for every index
        dist = [-1] * n

        for arr in positions.values():
            m = len(arr)

            if m == 1:
                continue

            for j in range(m):
                cur = arr[j]

                prev = arr[(j - 1) % m]
                nxt = arr[(j + 1) % m]

                d1 = abs(cur - prev)
                d1 = min(d1, n - d1)

                d2 = abs(cur - nxt)
                d2 = min(d2, n - d2)

                dist[cur] = min(d1, d2)

        return [dist[i] for i in queries]