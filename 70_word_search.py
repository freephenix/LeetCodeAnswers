class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        dict_map=[]
        for row in range(0, rows):
            temp =[]
            for col in range(0, cols):
                temp.append(False)
            dict_map.append(temp)


        for row in range(0, rows):
            for col in range(0, cols):
                if board[row][col] == word[0]:
                    if len(word)==1:
                        return True
                    flag = self.exist_(row, col, 0, word, board, dict_map)
                    if flag == True:
                        return True
        return False

    def exist_(self, row, col, size, word, board, dict_m):
        rows = len(board)
        cols = len(board[0])

        if size == len(word):
            return True

        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False

        if dict_m[row][col] == True:
            return False



        if board[row][col] == word[size]:
            dict_m[row][col] = True
            a=b=c=d=False

            a = self.exist_(row - 1, col, size + 1, word, board, dict_m)
            if a ==False:
                b = self.exist_(row, col + 1, size + 1, word, board, dict_m)
            else:
                dict_m[row][col] = False
                return True
            if b==False:
                c = self.exist_(row + 1, col, size + 1, word, board, dict_m)
            else:
                dict_m[row][col] = False
                return True
            if c==False:
                d = self.exist_(row, col - 1, size + 1, word, board, dict_m)
            else:
                dict_m[row][col] = False
                return True

            dict_m[row][col] = False
            return a or b or c or d

        else:
            return False     