class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hp = 0;
        np = 0; #TODO 初始位置？1可以吗
        max = 0;

        while(np != (s.__len__())):
            c = s[np];
            #print('c - ' + c);

            rp = hp;#重置位置
            flag = 0;#是否有相同标识
            while(rp < np):
                if(s[rp] == c):
                    flag = 1;
                    break;#跳出循环
                rp = rp + 1;

            if(flag ==  1):#更新子串头
                hp = rp + 1;

            if((np - hp + 1) > max):
                max = np - hp + 1;

            np = np + 1;#步进1

            # print("hp - ", hp);
            # print("np - ", np);
            # print("max - ", max);
            # print("### --- ");

        return max;


str = input()

solution = Solution();
print(solution.lengthOfLongestSubstring(str))
