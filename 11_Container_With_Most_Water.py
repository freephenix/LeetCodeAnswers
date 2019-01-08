class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        sp = 0
        ep = len(height) - 1
        maxArea = 0

        while(sp < ep):
            temp = (ep - sp) * min(height[sp], height[ep])
            if(temp > maxArea):
                maxArea = temp

            if(height[sp] > height[ep]):
                ep-=1
            else:
                sp+=1

        return maxArea


numList = [1,8,6,2,5,4,8,3,7]

solution = Solution()
print(solution.maxArea(numList))
