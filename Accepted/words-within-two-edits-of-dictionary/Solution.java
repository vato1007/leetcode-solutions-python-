import java.util.*;

class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        List<String> ans = new ArrayList<>();

        for (String query : queries) {

            for (String word : dictionary) {
                int differences = 0;

                for (int i = 0; i < query.length(); i++) {
                    if (query.charAt(i) != word.charAt(i)) {
                        differences++;
                    }

                    // Already more than 2 edits
                    if (differences > 2) {
                        break;
                    }
                }

                if (differences <= 2) {
                    ans.add(query);
                    break;
                }
            }
        }

        return ans;
    }
}