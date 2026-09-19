class Solution {

    // up, right, down, left
    int[][] dirs = {
        {-1, 0},
        {0, 1},
        {1, 0},
        {0, -1}
    };

    // Which directions each street connects to
    int[][] connections = {
        {},             // 0 unused
        {1, 3},         // 1: right, left
        {0, 2},         // 2: up, down
        {3, 2},         // 3: left, down
        {1, 2},         // 4: right, down
        {3, 0},         // 5: left, up
        {1, 0}          // 6: right, up
    };

    public boolean hasValidPath(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        boolean[][] visited = new boolean[m][n];

        return dfs(grid, 0, 0, visited);
    }

    private boolean dfs(int[][] grid, int r, int c,
                        boolean[][] visited) {

        int m = grid.length;
        int n = grid[0].length;

        if (r == m - 1 && c == n - 1) {
            return true;
        }

        visited[r][c] = true;

        int street = grid[r][c];

        for (int dir : connections[street]) {

            int nr = r + dirs[dir][0];
            int nc = c + dirs[dir][1];

            // Outside grid
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                continue;
            }

            // Already visited
            if (visited[nr][nc]) {
                continue;
            }

            // Neighbor must connect back
            int opposite = (dir + 2) % 4;

            boolean connectsBack = false;

            for (int d : connections[grid[nr][nc]]) {
                if (d == opposite) {
                    connectsBack = true;
                    break;
                }
            }

            if (connectsBack && dfs(grid, nr, nc, visited)) {
                return true;
            }
        }

        return false;
    }
}