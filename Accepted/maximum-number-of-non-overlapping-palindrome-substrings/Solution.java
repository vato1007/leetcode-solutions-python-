class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];

        // dp[i][j] = whether s[i..j] is a palindrome
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) &&
                    (j - i < 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                }
            }
        }

        int count = 0;
        int lastEnd = -1;

        // Process intervals by increasing ending position
        for (int end = 0; end < n; end++) {
            for (int start = 0; start <= end - k + 1; start++) {
                if (start > lastEnd && dp[start][end]) {
                    count++;
                    lastEnd = end;
                    break;
                }
            }
        }

        return count;
    }
}