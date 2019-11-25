class Solution:
    def nextPermutation(self, nums: list) -> None:
        point = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            # 查找第一队满足nums[i] < nums[i+1]的元素，若存在则表明下标i+1后面的元素都满足nums[i] > nums[i+1],即使降序序列
            if nums[i] < nums[i + 1]:
                # 若没有满足nums[i] < nums[i+1]的情况则整个序列是降序序列,则 firstIndex == -1
                point = i
                # 从序列最后一个元素开始找比firstIndex下标指向元素大的元素，也即是将下标firstIndex指向的元素按插入法排序插入到firstIndex后的降序序列中去
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        # 反转以firstIndex+1下标元素为起始元素的降序序列
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                break
        self.reverse(nums, point + 1, n - 1)

    def reverse(self, nums, i, j):
        """列表反转"""
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

numstr = "[1,2,4,3,1,2,4,3]"
nums = numstr.strip().strip('[]').split(',')

solution = Solution()
solution.nextPermutation(nums)
print(nums)
