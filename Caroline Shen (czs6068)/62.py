class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # initialize grid
        grid = [[0] * n for i in range(m)]

        # base case: first row and first column = 1
        for i in range (n):
            grid[0][i] = 1
        
        for i in range(m):
            grid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]
