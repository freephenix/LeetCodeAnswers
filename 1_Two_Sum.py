class Solution:
    def twoSum(self, nums, target):
        temp = {}
        t = int(target)
        for i,num in enumerate(nums):
            n = int(num)
            if n in temp:
                return [temp[n], i]
            else:
                temp[t - n] = i



# for line in sys.stdin:
#     nums = line
#     print(nums)
numstr = input()
target = input()

nums = numstr.strip().strip('[]').split(',')
# print(nums)
# print(target)

solution = Solution()
print(solution.twoSum(nums, target))

# solution = Solution()
# print(solution.twoSum([-1,-2,-3,-4,-5], -8))
