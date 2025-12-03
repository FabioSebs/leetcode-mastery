import { SlidingWindowDemo } from "../algorithms/sliding-window/main";
import { threeSums } from "../algorithms/two_pointers/main";
import { binarySearch } from "../algorithms/binary-search/main";

function TestSlidingWindowDemo(word: string) : number {
    return SlidingWindowDemo(word)
}

function TestTwoPointers(input : number[]) : number[][] {
    return threeSums(input)
}

function TestBinarySearch(input: number[], target: number) : number {
    return binarySearch(input, target)
}

function main() {
  console.log(TestBinarySearch([1,3,5,7,9,12,15,16,19,26,35,46,50], 16));
}

main();