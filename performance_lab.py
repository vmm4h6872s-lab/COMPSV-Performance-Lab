# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    most_common = numbers[0]

    for number in counts:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) because the function still goes through the list to count each number.
- Worst-case: O(n) because each number is processed once and dictionary lookups are usually O(1).
- Average-case: O(n) because the amount of work grows with the size of the input list.
- Space complexity: O(n) because the dictionary may have to store every number if they are all different.
- Why this approach? I used a dictionary because it makes it easy to keep track of how many times each number appears.
- Could it be optimized? This is already efficient for time. We could use less extra memory with a different approach, but it would probably take more time.
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) because the function still checks every number in the list.
- Worst-case: O(n) because each number is checked once and set lookups are usually O(1).
- Average-case: O(n) because the function goes through the input list one time.
- Space complexity: O(n) because the set and result list can grow based on the size of the input.
- Why this approach? I used a set to quickly check if a number was already seen and a list to keep the original order.
- Could it be optimized? The time complexity is already efficient. We could avoid using a set, but checking the result list for duplicates would make the solution slower.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        complement = target - number

        if complement in seen:
            pairs.append((complement, number))

        seen.add(number)

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) because the function goes through the list once.
- Worst-case: O(n) on average because set lookups are usually O(1) for each number.
- Average-case: O(n) because each number is processed one time.
- Space complexity: O(n) because the seen set can store up to n numbers and the pairs list stores the results.
- Why this approach? I used a set so I can quickly check if the number needed to reach the target was already seen.
- Could it be optimized? This is my optimized solution. My original approach would compare every number with every other number using nested loops, which would take O(n^2) time. Using a set improves the average time to O(n), but the trade-off is that it uses O(n) extra memory.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for i in range(n):
        if size == capacity:
            old_capacity = capacity
            capacity *= 2
            new_items = [None] * capacity

            for j in range(size):
                new_items[j] = items[j]

            items = new_items
            print("Resized from", old_capacity, "to", capacity)

        items[size] = i
        size += 1

    return items[:size]
"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize happens when the number of items reaches the current capacity of the list.
- What is the worst-case for a single append? O(n) because during a resize all of the existing elements have to be copied into the new list.
- What is the amortized time per append overall? O(1) because most appends do not require resizing.
- Space complexity: O(n) because the list grows based on the number of items being stored.
- Why does doubling reduce the cost overall? Doubling gives the list extra space, so a resize does not have to happen every time a new item is added. This spreads the expensive resizing operations across many normal appends.
"""

# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) because each number in the input list is processed once.
- Worst-case: O(n) because the function only needs one pass through the list.
- Average-case: O(n) because the amount of work grows directly with the size of the input.
- Space complexity: O(n) because a new result list is created with the same number of elements as the input.
- Why this approach? I used a running total so I do not have to go back and add the previous numbers again for every index.
- Could it be optimized? The time complexity is already O(n), which is efficient because every number has to be processed. It could use less extra space by changing the original list, but that would modify the input.
"""

# Test cases for Problem 1
assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
assert most_frequent([5, 5, 5]) == 5
assert most_frequent([1]) == 1
assert most_frequent([]) is None

# Test cases for Problem 2
assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
assert remove_duplicates([1, 1, 1, 1]) == [1]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []

# Test cases for Problem 3
assert set(find_pairs([1, 2, 3, 4], 5)) == {(1, 4), (2, 3)}
assert find_pairs([1, 2, 3], 10) == []
assert find_pairs([], 5) == []
assert set(find_pairs([-1, 0, 1, 2], 1)) == {(-1, 2), (0, 1)}

# Test cases for Problem 4
assert add_n_items(0) == []
assert add_n_items(1) == [0]
assert add_n_items(2) == [0, 1]
assert add_n_items(6) == [0, 1, 2, 3, 4, 5]

# Test cases for Problem 5
assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
assert running_total([5]) == [5]
assert running_total([]) == []
assert running_total([-1, 2, -3, 4]) == [-1, 1, -2, 2]
