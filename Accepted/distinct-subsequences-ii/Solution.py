class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        end = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            total = sum(end) % MOD

            # Every existing subsequence + ch
            # plus ch by itself
            end[i] = (total + 1) % MOD

        return sum(end) % MOD