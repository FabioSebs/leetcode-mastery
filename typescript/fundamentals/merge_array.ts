export function mergeArray() {
    const array1 : number[]= [1,2,3]
    const array2 : number[]= [4,5,6]

    // 1. spread operator
    const merged = [...array1, ...array2]
    console.log(merged)
    // 2. concat function
    const merged2 = array1.concat(array2)
    console.log(merged2)
}