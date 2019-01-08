class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1

        return res


nums = [-1, 2, 1, -4]
target = input()

solution = Solution()
print(solution.threeSumClosest(nums, int(target)))
