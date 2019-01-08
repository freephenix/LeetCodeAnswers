class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if(s.__len__() == 0):
            return ""

        #初始化变量
        max = 1;
        mstr = s[0];
        mp = 0.5
        while(mp < s.__len__() - 0.5):
            i = 1;
            if(mp % 1 == 0):
                while(((mp - i) > -1) & ((mp + i) < s.__len__())):
                    tmin = int(mp - i);
                    tmax = int(mp + i);
                    # print('1 - tmin', tmin);
                    # print('1 - tmax', tmax);
                    # print('1 - i', i);
                    if(s[tmin] == s[tmax]):
                        if ((2 * i + 1) > max):
                            max = 2 * i + 1;
                            mstr = s[tmin: tmax + 1];  # //切片，获取最长字段
                        i = i + 1;
                    else:
                        break;
            else:
                while(((mp - i + 0.5) > -1) & ((mp + i - 0.5) < s.__len__())):
                    tmin = int(mp - i + 0.5);
                    tmax = int(mp + i - 0.5);
                    # print('2 - tmin', tmin);
                    # print('2 - tmax', tmax);
                    # print('2 - i', i);
                    if(s[tmin] == s[tmax]):
                        if ((2 * i) > max):
                            max = 2 * i;
                            mstr = s[tmin: tmax + 1];  # //切片，获取最长字段
                        i = i + 1;
                    else:
                        break;

            mp = mp + 0.5;

        return mstr;


str   = input()
solution = Solution()
print(solution.longestPalindrome(str))
