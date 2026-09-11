class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        
        # dp[i] = minimum distance to repair the first i robots
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for position, limit in factory:
            new_dp = [float('inf')] * (n + 1)

            # Try repairing k robots at this factory
            for i in range(n + 1):
                distance = 0

                for k in range(0, min(limit, i) + 1):
                    if k > 0:
                        distance += abs(robot[i - k] - position)

                    new_dp[i] = min(
                        new_dp[i],
                        dp[i - k] + distance
                    )

            dp = new_dp

        return dp[n]