import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        heap = [(0, float('inf'))]

        for x, neg_height, right in events:

            # Remove buildings that have ended
            while heap[0][1] <= x:
                heapq.heappop(heap)

            # Start a new building
            if neg_height != 0:
                heapq.heappush(heap, (neg_height, right))

            current_height = -heap[0][0]

            # Only add a key point when height changes
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result