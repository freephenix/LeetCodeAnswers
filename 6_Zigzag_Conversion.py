class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # 定位字符
        yp = 0 # 行下标
        sp = 0 # s中字符下标
        rarr = ['' for i in range(numRows)] # 新建str数组, 存储每行字符串
        flag = 0 # Z字形走势方向
        while(sp < s.__len__()):
            if(flag == 0):
                if(yp < numRows - 1):
                    rarr[yp] = rarr[yp] + s[sp]
                    yp = yp + 1
                else:
                    flag = 1
                    rarr[yp] = rarr[yp] + s[sp]
                    yp = yp - 1
            else:
                if(yp > 0):
                    rarr[yp] = rarr[yp] + s[sp]
                    yp = yp - 1
                else:
                    flag = 0
                    rarr[yp] = rarr[yp] + s[sp]
                    yp = yp + 1
            sp = sp + 1

        #拼接字符串
        pp = 0
        rstr = ''
        while(pp < numRows):
            # print('pp str - ', rarr[pp])
            rstr = rstr + rarr[pp]
            pp = pp + 1

        return rstr


str   = input()
numRows = int(input())

solution = Solution()
print(solution.convert(str, numRows))



        # if numRows == 1: return s
        # lsit_con = [[] for i in range(numRows)] # 产生一个有numrows单元的list，每个list可以在后面添加元素
        # r = 0
        # direct = 1  # 行前进的方向是向上还是向下
        # for l in s:
        #     lsit_con[r].append(l)
        #     if r >= numRows - 1:
        #         direct = -1
        #     elif r == 0:
        #         direct = 1
        #     r += direct
        # answer = ""
        # for row in lsit_con:  # 按行优先打印出来
        #     answer += ''.join(row)
        #
        # print(answer)
