import { SlidingWindowDemo } from "../algorithms/sliding-window/main";

function TestSlidingWindowDemo(word: string) : number {
    return SlidingWindowDemo(word)
}

function main() {
  console.log(TestSlidingWindowDemo("fabiofabio"));
}

main();