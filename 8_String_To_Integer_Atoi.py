class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        #第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。         return 0
        #数字 "-91283472332" 超过 32 位有符号整数范围。因此返回 INT_MIN (−231) 。   return -2147483648 | 2147483647

        tstr = str.lstrip()

        if(tstr == ''):
            return 0

        if((tstr[0] != '+') & (tstr[0] != '-') & (not tstr[0].isdigit())):
            return 0

        signal = '+'
        if((tstr[0] == '-') | (tstr[0] == '+')):
            signal = tstr[0]
            tstr = tstr[1:]

        rstr = ''
        for ch in tstr:
            if(ch.isdigit()):
                rstr += ch
            else:
                break

        if(rstr == ''):
            return 0;

        rint = int(rstr)
        if(signal == '-'):
            if(rint > 2147483648):
                return -2147483648
            rint = 0 - rint
        else:
            if(rint > 2147483647):
                return 2147483647

        return rint


str   = input()

solution = Solution()
print(solution.myAtoi(str))

