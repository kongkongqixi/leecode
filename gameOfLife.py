class Solution:
    def is_1(self, lookup, board, i, j):
        # print(lookup[str(i)+str(j)])
        if lookup[str(i) +'_'+ str(j)] == 1:
            return 1 - board[i][j]
        else:
            return board[i][j]

    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        if len(board) == 0:
            return board
        col = len(board)
        row = len(board[0])
        lookup = defaultdict(str)
        for i in range(col):
            for j in range(row):
                sum_1 = 0
                if i == 12 and j == 0:
                    print(i,j )
                if i > 0:
                    sum_1 += self.is_1(lookup, board, i - 1, j)
                    if j > 0:
                        sum_1 += self.is_1(lookup, board, i - 1, j - 1)
                    if j < row - 1:
                        sum_1 += self.is_1(lookup, board, i - 1, j + 1)
                if i < col - 1:
                    sum_1 += self.is_1(lookup, board, i + 1, j)
                    if j > 0:
                        sum_1 += self.is_1(lookup, board, i + 1, j - 1)
                    if j < row - 1:
                        sum_1 += self.is_1(lookup, board, i + 1, j + 1)
                if j > 0:
                    sum_1 += self.is_1(lookup, board, i, j - 1)
                if j < row - 1:
                    sum_1 += self.is_1(lookup, board, i, j + 1)

                if sum_1 < 2 or sum_1 > 3:
                    if board[i][j] == 0:
                        continue
                    else:
                        board[i][j] = 0
                        lookup[str(i) +'_'+ str(j)] = 1
                elif sum_1 == 2:
                    continue
                elif sum_1 == 3:
                    if board[i][j] == 1:
                        continue
                    else:
                        board[i][j] = 1
                        lookup[str(i) +'_'+ str(j)] = 1
        return board


S = Solution()

print(S.gameOfLife([[1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0],[1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1],[0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,0],[1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1],[1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,0],[0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0],[0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0],[0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1],[1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1],[0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0],[0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,1],[0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1],[1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1],[1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0],[1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1]]))
