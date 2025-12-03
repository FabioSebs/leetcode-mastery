package main

import "fmt"

func main() {
	var (
		arr1 []int = []int{1, 2, 3}
		arr2 []int = []int{4, 5, 6}
	)

	// here is how to merge these arrays
	merged := append(arr1, arr2...)
	fmt.Println(merged)
}
