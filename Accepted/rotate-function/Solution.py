class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        # F(0)
        current = sum(i * nums[i] for i in range(n))
        ans = current

        # Calculate F(1), F(2), ..., F(n-1)
        for k in range(1, n):
            current += total - n * nums[n - k]
            ans = max(ans, current)

        return ans