class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkLine(board) and self.checkCol(board) and self.checkSqr(board)

    def checkLine(self, board: List[List[str]]) -> bool:
        for line in board:
            dict_line = defaultdict(int)
            for val in line:
                if val == ".":
                    continue
                else:
                    if dict_line[int(val)] < 1:
                        dict_line[int(val)] += 1
                    else:
                        return False
        return True
            
    def checkCol(self, board: List[List[str]]) -> bool:
        for i in range(9):
            dict_line = defaultdict(int)
            for j in range (9):
                val = board[j][i]
                if val == ".":
                    continue
                else:
                    if dict_line[int(val)] < 1:
                        dict_line[int(val)] += 1
                    else:
                        return False
        return True

    def checkSqr(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            dict_line = defaultdict(int)
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    val = board[row][col]
                    if val == ".":
                        continue
                    else:
                        if dict_line[int(val)] < 1:
                            dict_line[int(val)] += 1
                        else:
                            return False
        return True


        