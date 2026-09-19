class Solution {
    public boolean containsCycle(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    if (dfs(grid, visited, i, j, -1, -1)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] grid, boolean[][] visited,
                         int r, int c, int parentR, int parentC) {

        visited[r][c] = true;

        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];

            // Outside grid
            if (nr < 0 || nr >= grid.length ||
                nc < 0 || nc >= grid[0].length) {
                continue;
            }

            // Different character
            if (grid[nr][nc] != grid[r][c]) {
                continue;
            }

            // Don't immediately go back to parent
            if (nr == parentR && nc == parentC) {
                continue;
            }

            // Already visited -> cycle
            if (visited[nr][nc]) {
                return true;
            }

            // Continue DFS
            if (dfs(grid, visited, nr, nc, r, c)) {
                return true;
            }
        }

        return false;
    }
}