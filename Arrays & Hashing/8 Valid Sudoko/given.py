from typing import List 
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board:List[List[str]]) ->bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Key => (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
    
solution = Solution()
print(solution.isValidSudoku(
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","8",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","1",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]
))
print(solution.isValidSudoku(
    board=[["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]
))
print(solution.isValidSudoku(
    [[".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".","3",".","."],
     [".",".",".","1","8",".",".",".","."],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".",".","1",".","9","7","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".","3","6",".","1",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".","2","."]]
    ))

