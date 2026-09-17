class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int INF = n + 1;

        // best[i] = shortest target-sum subarray ending at or before i
        int[] best = new int[n];

        int left = 0;
        int sum = 0;
        int ans = INF;
        int minLen = INF;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            // Shrink window if sum is too large
            while (sum > target && left <= right) {
                sum -= arr[left++];
            }

            // Found a target-sum subarray
            if (sum == target) {
                int len = right - left + 1;

                // Need another subarray completely before 'left'
                if (left > 0 && best[left - 1] != INF) {
                    ans = Math.min(ans, len + best[left - 1]);
                }

                minLen = Math.min(minLen, len);
            }

            // Carry forward the best subarray seen so far
            best[right] = minLen;
        }

        return ans == INF ? -1 : ans;
    }
}