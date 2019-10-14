class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        import math
        up = int(math.fabs(dividend))
        down = int(math.fabs(divisor))
        result = 0
        while up >= down:
            base = down
            count = 1

            while up >= (base << 1):
                base <<= 1
                count <<= 1

            result += count
            up -= base

        if dividend ^ divisor < 0:
            result = -result

        if result < -(1 << 31) or result > ((1 << 31) - 1):
            result = (1 << 31) - 1

        return result


int1 = -2147483648
int2 = -1
solution = Solution()
print(solution.divide(int1, int2))
