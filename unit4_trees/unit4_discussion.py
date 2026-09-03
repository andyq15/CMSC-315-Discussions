"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

This program demonstrates how a Binary Search Tree (BST)
can be created, searched, and traversed.
"""


class Node:
    def __init__(self, value):
        # Each node stores a value and has references to
        # a left child and a right child.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # The root is the starting point of the BST.
        # None means the tree is initially empty.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST using recursion.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively insert a value into the correct position.
        """

        # If there is no node at this position, create a new one.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        # This allows the BST to eliminate larger values
        # when searching for a smaller value.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        # This allows the BST to eliminate smaller values
        # when searching for a larger value.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.

        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Returns True if the value is found and False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursively search for a value.
        """

        # Reaching None means the value is not in the tree.
        if node is None:
            return False

        # The value was found.
        if value == node.value:
            return True

        # If the value is smaller, only search the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the value is larger, only search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return the values from an in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Perform an in-order traversal:
        left subtree -> current node -> right subtree.
        """

        if node is None:
            return

        self._inorder_recursive(node.left, values)

        values.append(node.value)

        self._inorder_recursive(node.right, values)

        # Because smaller values are stored on the left and
        # larger values are stored on the right, an in-order
        # traversal produces the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    bst = BST()

    # These values create both left and right subtrees.
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)

    print("Values inserted:", values)

    # A BST reduces the search space at each step.
    # For example, if we are searching for 60 and start
    # at 50, we know 60 must be in the right subtree.
    # We do not need to search the entire left subtree.


    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = bst.inorder()

    print("In-order traversal:", traversal)

    # In-order traversal visits:
    # left subtree -> current node -> right subtree.
    # Because a BST stores smaller values on the left
    # and larger values on the right, the result is sorted.


    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Values that exist in the tree.
    print("Search for 40:", bst.search(40))
    print("Search for 80:", bst.search(80))

    # Values that do not exist in the tree.
    print("Search for 25:", bst.search(25))
    print("Search for 90:", bst.search(90))

    # BST searching is often more efficient than linear search
    # because each comparison tells us which subtree to search.
    # This allows us to eliminate a large portion of the tree.


    # ===============================
    # EDGE CASE
    # ===============================

    print("\n=== EDGE CASES ===")

    # Create an empty BST and search it.
    empty_bst = BST()

    print("Empty tree traversal:", empty_bst.inorder())
    print("Search for 50 in empty tree:", empty_bst.search(50))

    # An empty tree has no nodes, so its traversal returns
    # an empty list and searching returns False.


if __name__ == "__main__":
    main()
