"""
LC3: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
Example: 
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

# sliding window - dict
def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    max_length = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# sliding window - set
def lengthOfLongestSubstring_set(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window until s[right] is no longer duplicated
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Now we can safely add s[right]
        char_set.add(s[right])

        # Update max_length with current window size
        max_length = max(max_length, right - left + 1)

    return max_length

def lengthOfLongestSubstringFabrzySet(s : str) -> int: 
    character_set = set()
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # need a way to check if it is in set
        # if it is in set we remove or adjust the left
        while char in character_set:
            character_set.remove(char)
            left += 1 
        # we add to the char set 
        character_set.add(char)
        # update the max length
        max_length = max(max_length, right - left + 1)

    return max_length



if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    print(lengthOfLongestSubstring_set(s))
    print(lengthOfLongestSubstringFabrzySet(s))