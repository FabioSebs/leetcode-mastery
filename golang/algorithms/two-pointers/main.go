package main

import (
	"fmt"
	"sort"
)

func threeSums(nums []int) (res [][]int) {
	// This is a O(n log n) sort, where n is the length of the nums slice.
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	for idx, num := range nums {
		if idx > 0 && nums[idx] == nums[idx-1] {
			continue
		}

		left := idx + 1
		right := len(nums) - 1

		for left < right {
			total := num + nums[left] + nums[right]

			if total < 0 {
				left += 1
			} else if total > 0 {
				right -= 1
			} else {
				res = append(res, []int{num, nums[left], nums[right]})
			}

			leftVal := nums[left]
			for left < right && nums[left] == leftVal {
				left += 1
			}

			rightVal := nums[right]
			for left < right && nums[right] == rightVal {
				right -= 1
			}
		}
	}

	return
}

func main() {
	input := []int{
		-1, 0, 1, 2, -1, -4,
	}
	fmt.Println(threeSums(input))
}
