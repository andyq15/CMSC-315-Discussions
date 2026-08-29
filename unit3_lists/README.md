# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

Completing this assignment helped me better understand how Python lists handle insertion, deletion, and searching operations. I learned that inserting or deleting an item near the beginning or middle of a list can require other elements to shift positions, which can affect performance. I also practiced using the insert() and pop() methods and creating a linear search using a loop to check each element sequentially.

One challenge I encountered was understanding how to safely handle invalid indexes when deleting elements. I overcame this by validating that the index was within the list's valid range before attempting to remove an item. This prevents errors and allows the function to return None when an invalid index is provided. Another challenge was understanding why searching through an unsorted list can take longer as the list grows.

List operations can significantly impact performance in real-world applications, especially when working with large amounts of data. Frequent insertions or deletions near the beginning of a large list may be inefficient because many elements must be shifted. Understanding these performance differences can help programmers choose appropriate data structures for specific applications.
