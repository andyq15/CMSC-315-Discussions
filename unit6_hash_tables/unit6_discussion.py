"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program demonstrates how Python dictionaries work
similarly to hash tables. It shows insert, lookup, update,
delete, and edge-case operations.
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    # A Python dictionary works like a hash table because
    # each key is used to quickly find its associated value.
    # The key is processed using a hash function, which helps
    # Python locate the value efficiently.
    student_scores = {}

    # Add five key-value pairs to the dictionary.
    student_scores["Alice"] = 92
    student_scores["Bob"] = 85
    student_scores["Charlie"] = 78
    student_scores["Diana"] = 95
    student_scores["Ethan"] = 88

    print("\nDictionary contents:")
    print(student_scores)

    print("\n=== INSERT OPERATIONS ===")

    # Adding a new key inserts a new key-value pair into
    # the dictionary. The key is used to identify the value.
    student_scores["Frank"] = 90

    print("After inserting Frank:")
    print(student_scores)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary can quickly retrieve a value by using
    # its key. Python uses the key to locate the value.
    alice_score = student_scores["Alice"]
    charlie_score = student_scores["Charlie"]

    print("Alice's score:", alice_score)
    print("Charlie's score:", charlie_score)

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Dictionary before update:")
    print(student_scores)

    # Assigning a new value to an existing key updates
    # the value instead of creating another copy of the key.
    student_scores["Bob"] = 91

    print("\nDictionary after updating Bob's score:")
    print(student_scores)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Dictionary before deletion:")
    print(student_scores)

    # The del statement removes the specified key and
    # its associated value from the dictionary.
    del student_scores["Ethan"]

    print("\nDictionary after deleting Ethan:")
    print(student_scores)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a key that does not exist.
    # Using get() safely returns None instead of causing
    # a KeyError when the key is missing.
    missing_score = student_scores.get("George")

    print("Looking up George:")
    print("Result:", missing_score)

    # Edge Case 2: Safely deleting a key that may not exist.
    # pop() with a default value prevents a KeyError.
    removed_value = student_scores.pop("George", None)

    print("\nAttempting to delete George:")
    if removed_value is None:
        print("George was not found, so nothing was deleted.")
    else:
        print("George was deleted.")

    # Edge Case 3: Updating a key that does not exist.
    # Assigning a value to a new key creates a new
    # key-value pair instead of causing an error.
    student_scores["George"] = 82

    print("\nAfter adding George as a new key:")
    print(student_scores)

    print("\n=== PROGRAM COMPLETE ===")


if __name__ == "__main__":
    main()
