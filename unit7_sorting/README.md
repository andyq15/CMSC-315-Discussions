# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

While completing this assignment, I learned how Bubble Sort and Merge Sort work and how their approaches to sorting are different. I also practiced using loops, recursion, lists, and functions in Python. One of the biggest challenges I encountered was understanding how Merge Sort divides a list into smaller sections and then combines them back together in the correct order. I overcame this by breaking the process into smaller steps and understanding how the `merge() function compares values from each half.

Bubble Sort is easier to understand and implement because it repeatedly compares adjacent values and swaps them when they are out of order. However, it becomes less efficient as the list gets larger because its average and worst-case time complexity is O(n²). Merge Sort is more complex because it uses recursion and requires additional steps to merge the lists, but it is more efficient with a time complexity of O(n log n). Bubble Sort can be useful for small or simple datasets where ease of implementation is important. Merge Sort is a better choice when working with larger datasets where performance is more important. Overall, this assignment helped me understand that choosing a sorting algorithm depends on the size of the data and the tradeoffs involved.
