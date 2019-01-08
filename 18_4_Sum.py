import time

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # res为集合，可以去重
        res, dic = set(), {}
        # 获取数组nums的长度
        num_len = len(nums)
        # 排序，无返回值
        nums.sort()
        # 遍历0-num_len
        for i in range(num_len):
            # 遍历1到num_len
            for j in range(i+1, num_len):
                # 获取两者和
                key = nums[i] + nums[j]
                # 判断是否在dic字典中，不在的话，则把元组类型i,j的列表加入字典
                if key not in dic:  #.keys()
                    dic[key] = [(i, j)]
                else:
                    # 在dic中则加入相应key的列表中
                    dic[key].append((i, j))
        # 遍历0-num_len
        for i in range(num_len):
            # 遍历1-num_len-2
            for j in range(i+1, num_len-2):
                # exp作为目标值和两者的差，需要去dic中判断是否存在
                exp = target - nums[i] - nums[j]
                # 判断差值exp是否存在dic字典的keys中
                if exp in dic:  #.keys()
                    # 在dic中则遍历dic[exp]
                    for tmpIndex in dic[exp]:
                        # 如果tmpIndex[0]代表的i 大于 j 意味着四个值没有重复，加入结果结合中
                        if tmpIndex[0] > j:
                            # 集合会去重
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        # 对结果进行列表化
        return [list(i) for i in res]



start =time.clock()

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

end = time.clock()
print('Running time: %s Seconds'%(end-start))
