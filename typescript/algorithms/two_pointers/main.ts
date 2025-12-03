export function threeSums(nums : number[]) : number[][] {
    nums = nums.sort()
    const res = [] 

    for (let i = 0; i < nums.length; i++) {
        // base case for duplicates
        if (i > 0 && nums[i] == nums[i-1]) {
            continue
        }

        let left = i + 1
        let right = nums.length - 1
        
        while (left < right) {
            const total = nums[i]! + nums[left]! + nums[right]!
            
            if (total < 0) {
                left += 1
            } else if (total > 0) {
                right -= 1
            } else {
                res.push([nums[i]! , nums[left]! , nums[right]!])

                const leftValue = nums[left]
                while (left < right && leftValue === nums[left]) {
                    left += 1
                }

                const rightValue = nums[right]
                while (left < right && rightValue === nums[right]) {
                    right -=1
                }
            }
        }
    } 

    return res
} 