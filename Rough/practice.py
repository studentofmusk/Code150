from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set()
        negDiag = set()
        Cols = set()

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if (
                    c in Cols or
                    (r-c) in negDiag or
                    (r+c) in posDiag
                ):
                    continue
                Cols.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                board[r][c] = "Q"
                backtrack(r+1)

                Cols.remove(c)
                posDiag.remove((r+c))
                negDiag.remove((r-c))
                board[r][c] = "."
        backtrack(0)

        return res

