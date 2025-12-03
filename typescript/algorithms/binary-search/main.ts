export function binarySearch(nums : number[], target : number) : number {
    let left = 0
    let right = nums.length -1 

    while ( left <= right) {
        const mid : number = Math.floor((left+right)/2) 
        const midVal = nums[mid]
        if (midVal == target) {
            return mid
        }
        else if (midVal! < target ) {
            left = mid + 1
        }
        else {
            right = mid - 1
        }
    }   
    return -1
} 