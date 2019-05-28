class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nowp = 0
        lastp = len(nums)
        while nowp < lastp:
            if nums[nowp] == val:
                nums[nowp] = nums[lastp]
                lastp = lastp - 1
            nowp = nowp + 1
        return lastp
