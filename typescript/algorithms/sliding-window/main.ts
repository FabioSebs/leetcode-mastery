export function SlidingWindowDemo(word : string) : number {
    let left : number = 0
    let max_length : number = 0  
    const character_set = new Map<string, boolean>();
    
    for (let i = 0; i < word.length; i++) {
        while (character_set.get(word[i] as string)) { 
            character_set.delete(word[i] as string)
            left+=1
        }

        character_set.set(word[i] as string, true)
        max_length = (i - left) + 1
    }

    return max_length
}