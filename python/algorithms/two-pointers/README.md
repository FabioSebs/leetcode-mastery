# LC15: 3Sum (Two Pointers)

**Problem**

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`, and
- `nums[i] + nums[j] + nums[k] == 0`.

The solution set **must not** contain duplicate triplets.

Example:

- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[−1, −1, 2], [−1, 0, 1]]`

This is a classic use case for the **two-pointers** pattern on a **sorted** array.

---

## High-Level Idea

1. **Sort** the array first.
2. Iterate over the array, treating `nums[i]` as the **first** element of the triplet.
3. For the remaining part of the array (`[i+1 .. n-1]`), use **two pointers**:
   - `left` starts at `i + 1`.
   - `right` starts at `n - 1`.
4. Compute the sum: `total = nums[i] + nums[left] + nums[right]`.
   - If `total < 0`: we need a **larger** sum → move `left` right (`left += 1`).
   - If `total > 0`: we need a **smaller** sum → move `right` left (`right -= 1`).
   - If `total == 0`: we found a valid triplet → add it to the result, then move both pointers while **skipping duplicates**.
5. While iterating `i`, also **skip duplicates** of `nums[i]` so you don’t generate the same triplet multiple times.

Sorting is what makes this work:

- It allows you to move `left` and `right` deterministically based on whether the current sum is too small or too large.
- It makes duplicate values adjacent, so you can easily skip them.

---

## Implementation Overview (`threeSums`)

The function in `main.py`:

```python
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
```

### Key Points

- **Sorting**: `nums.sort()` is required to use the two-pointers logic and to skip duplicates reliably.
- **Outer loop (`i`)**: picks the first element of the triplet.
  - `if i > 0 and nums[i] == nums[i - 1]: continue` ensures we don’t start from the same value twice.
- **Inner loop (`left`, `right`)**: searches for pairs that, together with `nums[i]`, sum to `0`.
- **Duplicate skipping inside the window**:
  - After finding a valid triplet, we move `left` forward while the value stays the same.
  - Similarly, we move `right` backward while the value stays the same.
  - This prevents generating the same triplet multiple times.

---

## Complexity

- **Time Complexity:**
  - Sorting: `O(n log n)`.
  - For each index `i`, the two-pointer scan is `O(n)` in the worst case.
  - Overall: `O(n^2)`.

- **Space Complexity:**
  - `O(1)` additional space (ignoring the space for the output), since we sort in-place and use only a few pointers and variables.

---

## How to Use

Example usage (in a `__main__` block or separate test):

```python
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSums(nums))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
```

This will run the two-pointers 3Sum solution and print all unique triplets that sum to zero.

