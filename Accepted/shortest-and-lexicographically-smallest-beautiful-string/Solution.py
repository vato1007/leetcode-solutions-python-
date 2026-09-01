class Solution:
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                # Remove leading zeros while keeping exactly k ones
                while left <= right and s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                if best == "" or len(curr) < len(best):
                    best = curr
                elif len(curr) == len(best) and curr < best:
                    best = curr

        return best