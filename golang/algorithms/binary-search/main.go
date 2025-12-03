package main

import (
	"fmt"
	"math/rand"
)

func BinarySearch(nums []int, target int) (index int) {
	fmt.Printf("target : %d\n", target)

	var (
		left  int = 0
		right int = len(nums) - 1
	)

	for left <= right {
		mid := (left + right) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return -1
}

func main() {
	nums := []int{1, 3, 5, 7, 9, 12, 15, 16, 19, 26, 35, 46, 50}
	min := 0
	max := len(nums) - 1
	randIndex := rand.Intn(max - min + 1)
	fmt.Println(BinarySearch(nums, nums[randIndex]))
}
