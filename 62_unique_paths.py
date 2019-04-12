class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n,m=max(m,n),min(m,n)
        
        mult_1=1
        for i in range(n,n+m-1):
            mult_1*=i
        mult_2=1
        for i in range(1,m):
            mult_2*=i
        return int(mult_1/mult_2)