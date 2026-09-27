"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

This program demonstrates two sorting algorithms:
- Bubble Sort
- Merge Sort

It compares their results using two datasets and tests
several edge cases.
"""


def bubble_sort(lst):
    """
    Sort a list using the Bubble Sort algorithm.

    A copy of the original list is created so the original
    list is not changed.
    """
    # Create a copy so the original list remains unchanged.
    sorted_list = lst.copy()

    # Compare adjacent elements and swap them when needed.
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j],
                )

    return sorted_list


def merge_sort(lst):
    """
    Sort a list using the Merge Sort algorithm.

    Merge Sort divides the list into smaller halves,
    recursively sorts each half, and then merges them.
    """
    # A list with zero or one item is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list.
    middle = len(lst) // 2

    # Recursively sort the left and right halves.
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # Merge the sorted halves.
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """
    result = []
    left_index = 0
    right_index = 0

    # Compare values from both lists and add the smaller value.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list.
    result.extend(left[left_index:])

    # Add any remaining values from the right list.
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================

    print("\n=== DATASET #1 ===")

    dataset1 = [64, 25, 12, 22, 11, 90, 34]

    print("Original list:", dataset1)

    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # ===============================
    # DATASET #2
    # ===============================

    print("\n=== DATASET #2 ===")

    dataset2 = [45, 7, 89, 23, 7, 56, 14, 32]

    print("Original list:", dataset2)

    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    # Compare the results.
    if bubble_result2 == merge_result2:
        print("Both algorithms produced the same sorted result.")
    else:
        print("The algorithms produced different results.")

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    empty_list = []
    print("\nEmpty list:")
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))
    print("An empty list is already sorted.")

    # Edge case 2: List with duplicate values.
    duplicate_list = [5, 2, 5, 1, 2, 5]
    print("\nList with duplicate values:")
    print("Original:", duplicate_list)
    print("Bubble Sort:", bubble_sort(duplicate_list))
    print("Merge Sort:", merge_sort(duplicate_list))
    print("Duplicate values are kept in the sorted list.")

    # Edge case 3: Already sorted list.
    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready sorted list:")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))
    print("The list remains in sorted order.")


if __name__ == "__main__":
    main()
