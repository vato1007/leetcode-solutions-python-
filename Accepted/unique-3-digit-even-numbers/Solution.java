class Solution {
    public int totalNumbers(int[] digits) {
        int[] count = new int[10];

        // Count available copies of each digit
        for (int digit : digits) {
            count[digit]++;
        }

        int ans = 0;

        // Every 3-digit even number
        for (int num = 100; num <= 998; num += 2) {
            int a = num / 100;
            int b = (num / 10) % 10;
            int c = num % 10;

            // Check whether we have enough copies
            int[] need = new int[10];
            need[a]++;
            need[b]++;
            need[c]++;

            boolean possible = true;

            for (int d = 0; d <= 9; d++) {
                if (need[d] > count[d]) {
                    possible = false;
                    break;
                }
            }

            if (possible) {
                ans++;
            }
        }

        return ans;
    }
}