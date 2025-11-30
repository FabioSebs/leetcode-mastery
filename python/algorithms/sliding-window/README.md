# LC3: Longest Substring Without Repeating Characters
===================================================

**Problem**

Given a string `s`, find the length of the longest substring without repeating characters.

Example:

- Input: `"abcabcbb"`
- Output: `3`
- Explanation: The answer is `"abc"`, which has length `3`.

This is a classic **sliding window** problem.

Sliding Window Idea
-------------------

We maintain a window `[left, right]` over the string such that:

- All characters inside the window are unique.
- We expand `right` step by step.
- When we detect a duplicate, we move `left` forward just enough to restore the "no duplicates" property.

At each step, we update the answer with the current window size: `right - left + 1`.

Approach 1: Sliding Window + Dict (Index Map)
--------------------------------------------

Function: `lengthOfLongestSubstring(s: str) -> int`

Key ideas:

- Use a dictionary `last_seen: dict[char, int]` to store the **last index** where each character appeared.
- Iterate with `right` over the string using `enumerate`.
- When we see a character `ch` that we have seen before **inside the current window** (i.e. `last_seen[ch] >= left`), we move `left` to `last_seen[ch] + 1`.
- Update `last_seen[ch] = right`.
- Track `max_length = max(max_length, right - left + 1)`.

This gives an `O(n)` time solution, because each character index is processed at most twice: once when `right` visits it, and possibly once when `left` jumps forward.

Approach 2: Sliding Window + Set
--------------------------------

Function: `lengthOfLongestSubstring_set(s: str) -> int`

Key ideas:

- Use a set `char_set` to store the characters currently in the window.
- Use two pointers `left` and `right`.
- For each `right`:
  - While `s[right]` is already in `char_set`, shrink the window from the left:
    - Remove `s[left]` from the set.
    - Increment `left`.
  - Add `s[right]` to the set.
  - Update `max_length` with the current window size: `right - left + 1`.

This also runs in `O(n)` time, since each character is added to and removed from the set at most once.

Complexity
----------

For both approaches:

- **Time Complexity:** `O(n)`, where `n` is the length of the string.
- **Space Complexity:** `O(k)`, where `k` is the size of the character set used in the string (at most `n`).

How to Run
----------

From this directory:

```bash
python3 main.py
```

The `__main__` block in `main.py` calls the sliding window implementations and prints the length of the longest substring without repeating characters for a sample input.

