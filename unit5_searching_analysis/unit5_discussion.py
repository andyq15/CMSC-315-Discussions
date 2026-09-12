"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

This program demonstrates and compares linear search and
binary search using small and large datasets.
"""


def linear_search(lst, target):
    """
    Search for a target using linear search.

    Linear search checks each item from the beginning of the
    list until the target is found. Since it may need to check
    every item, its worst-case time complexity is O(n).
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    Search for a target using binary search.

    Binary search assumes the list is sorted. Each iteration
    checks the middle value and eliminates half of the
    remaining search space. This gives binary search an
    O(log n) time complexity.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position of the current search space.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        if lst[middle] < target:
            # Target must be in the right half.
            left = middle + 1
        else:
            # Target must be in the left half.
            right = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # This is a small sorted list that will be used
    # to test both search algorithms.
    small_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    target_exists = 50
    target_missing = 55

    print("Dataset:", small_data)

    # Test a value that exists.
    linear_result = linear_search(small_data, target_exists)
    binary_result = binary_search(small_data, target_exists)

    print(f"\nSearching for {target_exists}:")
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms should find 50 at index 4.
    # Linear search checks values from the beginning.
    # Binary search reaches the middle of the list much faster.

    # Test a value that does not exist.
    linear_result = linear_search(small_data, target_missing)
    binary_result = binary_search(small_data, target_missing)

    print(f"\nSearching for {target_missing}:")
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms return -1 because 55 is not in the list.

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted dataset containing 10,000 values.
    large_data = list(range(1, 10001))

    target_large = 9999

    print("Dataset size:", len(large_data))
    print(f"Searching for {target_large}...")

    linear_result = linear_search(large_data, target_large)
    binary_result = binary_search(large_data, target_large)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Linear search may have to examine almost every item
    # before finding a value near the end of a large list.
    #
    # Binary search repeatedly cuts the search area in half.
    # For 10,000 values, it only needs around log2(10,000)
    # comparisons instead of potentially checking all 10,000.
    #
    # Therefore, binary search becomes much more efficient
    # as the dataset becomes larger.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\n1. Empty list:")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # Both searches return -1 because there are no elements
    # in the list.

    # Edge Case 2: Single-element list
    single_list = [25]

    print("\n2. Single-element list:")
    print("Dataset:", single_list)
    print("Searching for 25:")
    print("Linear search:", linear_search(single_list, 25))
    print("Binary search:", binary_search(single_list, 25))

    # Both algorithms return index 0 because 25 is the only
    # element in the list.

    # Edge Case 3: Value not present
    print("\n3. Value not present:")
    print("Dataset:", small_data)
    print("Searching for 100:")
    print("Linear search:", linear_search(small_data, 100))
    print("Binary search:", binary_search(small_data, 100))

    # Both algorithms return -1 because 100 is not present.


if __name__ == "__main__":
    main()
