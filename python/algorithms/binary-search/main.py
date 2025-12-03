from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:  # mid_val > target
            right = mid - 1

    return -1  # not found
 

if __name__ == "__main__":
    input = [1,3,5,7,9,12,15,16,19,26,35,46,50]
    print(binarySearch(input, 16))