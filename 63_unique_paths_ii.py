class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        动态规划，基于62题改进
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [([0] * n) for i in range(m)]

        for i in range(0,m):
            # 如果有1，则memo中这个和这之后的都为0，不需要改变
            if obstacleGrid[i][0] ==1:
                break
            memo[i][0]=1

        for j in range(0,n):
            if obstacleGrid[0][j] ==1:
                break
            memo[0][j]=1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] !=1:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m-1][n-1]