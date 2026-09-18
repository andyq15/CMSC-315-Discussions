# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

Completing this assignment helped me better understand how Python dictionaries work and how they are related to hash tables. I learned how to insert, look up, update, and delete key-value pairs in a dictionary. I also learned that dictionaries use keys to locate values, which allows information to be accessed efficiently without searching through every item.

One challenge I encountered was understanding what happens when a key does not exist in the dictionary. I learned that using methods such as get() and pop() with a default value can prevent errors when working with missing keys. Writing comments in the program also helped me understand what each operation was doing and why it was useful.

Hash tables use a hash function to convert a key into an index or location where the associated value can be stored. A collision occurs when two different keys produce the same hash location. Hash tables handle collisions using techniques such as chaining or probing. Because hash tables can usually find values in constant average time, O(1), they can be much more efficient than searching through every item one at a time. Overall, this assignment gave me a better understanding of how dictionaries and hash tables are used to organize and access data efficiently.
