class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = '';
        if (x > -2147483648) and (x < 2147483647):
            if(x < 0):
                for s in str(-x):
                    string = s + string

                if(int(string) > 2147483648):
                    return 0;
                else:
                    return -int(string)
            elif(x > 0):
                for s in str(x):
                    string = s + string

                if(int(string) > 2147483647):
                    return 0;
                else:
                    return int(string);
            else:
                return 0;
        else:
            return 0;


"""
    注意点：
        1、反转前的判断，32位数的范围是 -2^31, 2^31-1
        2、反转后的判断，范围依然应该满足第一条的范围
"""


num = -8147483611

solution = Solution()
print(solution.reverse(num))
