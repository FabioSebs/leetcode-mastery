package main

import "fmt"

func SlidingWindowDemo(s string) int {
	seen := make(map[byte]bool)
	left := 0
	maxLen := 0

	for right := 0; right < len(s); right++ {
		// Shrink window until s[right] is no longer in the set
		for seen[s[right]] {
			delete(seen, s[left])
			left++
		}

		// Add current character to the window
		seen[s[right]] = true

		// Update maxLen
		curLen := right - left + 1
		if curLen > maxLen {
			maxLen = curLen
		}
	}

	return maxLen
}

func main() {
	word := "fabrzyfabrzy"
	fmt.Println(SlidingWindowDemo(word))
}
