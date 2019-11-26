package main

import "fmt"

func nextPermutation(nums []int) {
	n := len(nums)
	var i = n - 1
	for ; i > 0; i-- {
		if nums[i] > nums[i-1] {
			j := i
			for j < n && nums[j] > nums[i-1] {
				j++
			}
			nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
			break
		}
	}
	// sort.Ints(nums[i:])

	var k = n - 1
	for k >= i {
		nums[k], nums[i] = nums[i], nums[k]
		k--
		i++
	}
}

func main() {
	var nums = []int{1, 2, 3, 4, 6, 2, 4, 5, 3, 2, 1}
	nextPermutation(nums)

	mySlice := nums[0:]
	fmt.Println(mySlice)
}
