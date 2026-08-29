"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

This program demonstrates inserting, deleting, and searching for
elements in a Python list.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # When a value is inserted, existing elements at and after the
    # specified index are shifted one position to the right.
    # Inserting near the beginning is generally slower because more
    # elements must be shifted. Inserting at the end is generally faster.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    """
    # Index validation prevents an IndexError and allows the program
    # to safely handle invalid deletion requests.
    if 0 <= index < len(lst):
        # Removing an element causes the elements after it to shift
        # one position to the left.
        return lst.pop(index)

    return None


def search_value(lst, value):
    """
    Search for a value within the list and return its index.
    """
    # This is a linear search because each element is checked
    # sequentially from the beginning until the value is found.
    for index, item in enumerate(lst):
        if item == value:
            return index

    return -1


def main():
    """Run demonstrations of list operations."""
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # Create the original list.
    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)

    # Insert a value at the beginning.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Insert a value in the middle.
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 25)
    print("After inserting 25 in the middle:", numbers)

    # Insert a value at the end.
    insert_at(numbers, len(numbers), 60)
    print("After inserting 60 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # Delete the first item in the list.
    removed = delete_at(numbers, 0)
    print("Removed from the beginning:", removed)
    print("Updated list:", numbers)

    # Delete an item from the middle.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print("Removed from the middle:", removed)
    print("Updated list:", numbers)

    # Delete the last item in the list.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from the end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists in the list.
    search_result = search_value(numbers, 30)

    if search_result != -1:
        print("Value 30 found at index:", search_result)
    else:
        print("Value 30 was not found.")

    # Search for a value that does not exist.
    search_result = search_value(numbers, 100)

    if search_result != -1:
        print("Value 100 found at index:", search_result)
    else:
        print("Value 100 was not found.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to delete using an invalid index.
    removed = delete_at(numbers, 100)
    print("Attempt to delete index 100:", removed)

    # Edge case 2: Insert a value into an empty list.
    empty_list = []
    print("Empty list before insertion:", empty_list)

    insert_at(empty_list, 0, 99)
    print("Empty list after inserting 99:", empty_list)

    # Edge case 3: Attempt to delete from an empty list.
    empty_list = []
    removed = delete_at(empty_list, 0)
    print("Attempt to delete from an empty list:", removed)


if __name__ == "__main__":
    main()
