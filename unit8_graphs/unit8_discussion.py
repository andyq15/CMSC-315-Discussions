"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

This program demonstrates Breadth-First Search (BFS) using
an adjacency-list graph.
===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph.

    BFS uses a queue so that nodes are visited level by level.
    A visited set prevents nodes from being visited more than once.
    """

    # Check if the starting node exists in the graph.
    if start not in graph:
        return []

    visited = set()
    queue = deque()

    # Add the starting node to the queue and mark it visited.
    queue.append(start)
    visited.add(start)

    traversal_order = []

    while queue:
        # A queue is used because BFS visits nodes in the order
        # they are discovered, moving through the graph level by level.
        current = queue.popleft()
        traversal_order.append(current)

        # Add unvisited neighbors to the queue so they can be
        # processed after the current level has been explored.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    #
    # Each node represents a building on a college campus.
    # Each edge represents a walking path between buildings.
    #
    # The graph is represented using an adjacency list.

    graph = {
        "Library": ["Student Center", "Science Hall"],
        "Student Center": ["Library", "Gym", "Cafeteria"],
        "Science Hall": ["Library", "Engineering"],
        "Gym": ["Student Center", "Cafeteria"],
        "Cafeteria": ["Student Center", "Gym", "Engineering"],
        "Engineering": ["Science Hall", "Cafeteria"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ===============================
    # BFS TRAVERSAL
    # ===============================

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Library"
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print("BFS traversal order:")
    print(" -> ".join(traversal))

    # BFS visits nodes level by level.
    # Starting at the Library, BFS first visits the Library's
    # direct neighbors before moving farther away.

    # ===============================
    # ADDITIONAL EDGE
    # ===============================

    print("\n=== UPDATED GRAPH ===")

    # Add a new connection between the Library and Engineering.
    graph["Library"].append("Engineering")
    graph["Engineering"].append("Library")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    updated_traversal = bfs(graph, start_node)

    print("\nUpdated BFS traversal order:")
    print(" -> ".join(updated_traversal))

    # ===============================
    # EDGE CASE TESTS
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Start from a different node.
    different_start = "Gym"
    result = bfs(graph, different_start)

    print(f"\nEdge Case 1 - Starting from {different_start}:")
    print(" -> ".join(result))

    # Edge Case 2: Start node does not exist.
    missing_start = "Parking Lot"
    result = bfs(graph, missing_start)

    print("\nEdge Case 2 - Missing starting node:")
    if not result:
        print(f"'{missing_start}' is not in the graph, so BFS returns an empty list.")

    # ===============================
    # BFS VS DFS
    # ===============================

    print("\n=== BFS VS DFS ===")
    print("BFS uses a queue and explores nodes level by level.")
    print("DFS uses a stack or recursion and explores as far as possible")
    print("along one path before backtracking.")


if __name__ == "__main__":
    main()
