"""
LC15: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example: 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List
def threeSums(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res: List[List[int]] = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for nums[left]
                left_val = nums[left]
                while left < right and nums[left] == left_val:
                    left += 1

                # Skip duplicates for nums[right]
                right_val = nums[right]
                while left < right and nums[right] == right_val:
                    right -= 1

    return res

def threeSumsFabrzy(nums : List[int]) -> List[List[int]]:
    # first step is to sort ascendingly
    nums.sort()
    res : List[List[int]] = []
    n = len(nums)

    for i in range(n):
        # need a base case to see if i is left or a duplicate value
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            # lets calculate total of current, left, and right and validate if it equals to 0
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                
                left_val = nums[left]
                while left < right and nums[left] == left_val:
                    left += 1

                right_val = nums[right]
                while left < right and nums[right] == right_val:
                    right -= 1

    return res

if __name__ == "__main__":
    input = [-1,0,1,2,-1,-4]
    print(threeSumsFabrzy(input))