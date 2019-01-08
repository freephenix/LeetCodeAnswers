class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # prefix = ''
        # i = 0
        # while True:
        #     try:
        #         tmp = strs[0][i]
        #         for item in strs:
        #             if item[i] != tmp:
        #                 return prefix
        #     except: #out of index range，表明遍历最短字符串完毕
        #         return prefix
        #     prefix += tmp
        #     i += 1
        # return prefix


    # def longestCommonPrefix_use_zip(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
        prefix = ''
        for _, item in enumerate(zip(*strs)):
            if len(set(item)) > 1:
                return prefix
            else:
                prefix += item[0]
        return prefix
