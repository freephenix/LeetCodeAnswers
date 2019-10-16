package main

func divide(dividend int, divisor int) int {
	if dividend == -(1 << 31) {
		if divisor == -1 {
			return 1<<31 - 1
		}
		if divisor == 1 {
			return -(1 << 31)
		}
	}
	positive := false
	if dividend > 0 && divisor > 0 || dividend < 0 && divisor < 0 {
		positive = true
	}

	if dividend > 0 {
		dividend = -dividend
	}
	if divisor > 0 {
		divisor = -divisor
	}

	_, ans := dfs(dividend, divisor, 1)

	if positive {
		return ans
	} else {
		return -ans
	}
}

func dfs(dividend, divisor int, count int) (int, int) {
	if dividend > divisor {
		return dividend, 0
	}

	d, c := dfs(dividend, divisor+divisor, count+count)
	if d <= divisor {
		return d - divisor, count + c
	}

	return d, c
}

func main() {
	dividend := -2147483648
	divisor := -1
	res := divide(dividend, divisor)

	println(res)
}
