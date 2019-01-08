class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]:    # skip duplicates
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans

# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         import operator
#
#         returnList = []
#         listPositive = []
#         listZero = []
#         listNegative = []
#         for x in nums:
#             if x == 0:
#                 listZero.append(x)
#             elif x > 0:
#                 listPositive.append(x)
#             else:
#                 listNegative.append(x)
#
#         # 全是0的情况
#         if len(listZero) > 2:
#             returnList.append([0,0,0])
#
#         # 一个正数一个负数一个零的情况
#         if len(listZero) >= 1:
#             for x in listPositive:
#                 if -x in listNegative:
#                     listTemp = sorted([x, -x, 0])
#                     if listTemp not in returnList:
#                         returnList.append(listTemp)
#
#         # 两个正数一个负数的情况
#         for (k_x,x) in enumerate(listPositive):
#             for (k_y,y) in enumerate(listPositive):
#                 if ((k_x != k_y) & (-(x+y) in listNegative)):
#                     listTemp = sorted([x, y, -(x+y)])
#                     if listTemp not in returnList:
#                         returnList.append(listTemp)
#
#         # 两个负数一个正数的情况
#         for (k_x,x) in enumerate(listNegative):
#             for (k_y,y) in enumerate(listNegative):
#                 if ((k_x != k_y) & (-(x+y) in listPositive)):
#                     listTemp = sorted([x, y, -(x+y)])
#                     if listTemp not in returnList:
#                         returnList.append(listTemp)
#
#         # 返回结果
#         return returnList



nums = [1,2,3,4,0,0,0,-1,-2,-3]

solution = Solution()
print(solution.threeSum(nums))
