# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

While completing this assignment, I learned how a Binary Search Tree (BST) stores and organizes data using nodes and references to left and right children. I also learned how to implement important BST operations, including insertion, searching, and in-order traversal. One challenge I encountered was understanding the recursive methods because the function repeatedly calls itself on different parts of the tree. I overcame this by breaking the process down into smaller steps and understanding what happens when the current node is either empty, smaller, or larger than the value being searched or inserted.

A BST is efficient because it keeps values ordered. Smaller values are placed on the left and larger values are placed on the right, allowing the search to eliminate an entire subtree at each step. An in-order traversal also produces the values in sorted order. Compared to a basic array or linked list, where searching may require checking each element one at a time, a balanced BST can find values much faster, with an average time of O(log n). However, an unbalanced BST can become less efficient and approach O(n), similar to a linear search.
