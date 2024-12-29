class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        for r in range(m-1, -1, -1):
            curRow = [0] * n
            curRow[n-1] = 1
            for c in range(n-2, -1, -1):
                curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow

        return prevRow[0]

#
# There is an m x n grid where you are allowed to move either down or to the right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
#
# You may assume the output will fit in a 32-bit integer.
#
# Example 1:
#
# Input: m = 3, n = 6
#
# Output: 21
#
# Example 2:
#
# Input: m = 3, n = 3
#
# Output: 6
#
# Constraints:
#
#     1 <= m, n <= 100
#