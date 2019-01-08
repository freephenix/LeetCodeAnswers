class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        inList = list(s)
        leftList = []

        for i in range(0, len(inList)):
            if (len(leftList) == 0):  # 第一个字符
                if ((inList[i] == '[') | (inList[i] == '{') | (inList[i] == '(')):
                    leftList.insert(0, inList[i])
                else:
                    return False
            else:
                if((inList[i] == '[') | (inList[i] == '{') | (inList[i] == '(')):
                    leftList.insert(0, inList[i])
                elif(((leftList[0] == '{') & (inList[i] == '}')) | ((leftList[0] == '[') & (inList[i] == ']')) | ((leftList[0] == '(') & (inList[i] == ')'))):
                    leftList.pop(0)
                else:
                    return False

        #匹配结束
        if(len(leftList) == 0):
            return True
        else:
            return False


str = '[}'

solution = Solution()
print(solution.isValid(str))
