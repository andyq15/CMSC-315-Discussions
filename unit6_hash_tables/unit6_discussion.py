import java.util.HashMap;
import java.util.Map;

"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

This program demonstrates how Python dictionaries work
similarly to hash tables. It shows insert, lookup, update,
delete, and edge-case operations.
"""

public class Unit6Discussion {

    public static void main(String[] args) {

        System.out.println("=== UNIT 6: DICTIONARIES AS HASH TABLES ===");

        // ===============================
        // CREATE A HASH TABLE
        // ===============================

        // A Java HashMap works similarly to a hash table.
        // Each key is used to locate its associated value.
        Map<String, Integer> studentScores = new HashMap<>();

        // Add five key-value pairs to the HashMap.
        studentScores.put("Alice", 92);
        studentScores.put("Bob", 85);
        studentScores.put("Charlie", 78);
        studentScores.put("Diana", 95);
        studentScores.put("Ethan", 88);

        System.out.println("\nHashMap contents:");
        System.out.println(studentScores);

        // ===============================
        // INSERT OPERATIONS
        // ===============================

        System.out.println("\n=== INSERT OPERATIONS ===");

        // Adding a new key inserts a new key-value pair.
        studentScores.put("Frank", 90);

        System.out.println("After inserting Frank:");
        System.out.println(studentScores);

        // ===============================
        // LOOKUP OPERATIONS
        // ===============================

        System.out.println("\n=== LOOKUP OPERATIONS ===");

        // get() retrieves the value associated with a key.
        Integer aliceScore = studentScores.get("Alice");
        Integer charlieScore = studentScores.get("Charlie");

        System.out.println("Alice's score: " + aliceScore);
        System.out.println("Charlie's score: " + charlieScore);

        // ===============================
        // UPDATE OPERATIONS
        // ===============================

        System.out.println("\n=== UPDATE OPERATIONS ===");

        System.out.println("HashMap before update:");
        System.out.println(studentScores);

        // Putting a new value with an existing key updates
        // the value associated with that key.
        studentScores.put("Bob", 91);

        System.out.println("\nHashMap after updating Bob's score:");
        System.out.println(studentScores);

        // ===============================
        // DELETE OPERATIONS
        // ===============================

        System.out.println("\n=== DELETE OPERATIONS ===");

        System.out.println("HashMap before deletion:");
        System.out.println(studentScores);

        // remove() deletes the specified key and its value.
        studentScores.remove("Ethan");

        System.out.println("\nHashMap after deleting Ethan:");
        System.out.println(studentScores);

        // ===============================
        // EDGE CASES
        // ===============================

        System.out.println("\n=== EDGE CASES ===");

        // Edge Case 1: Looking up a key that does not exist.
        // get() returns null instead of causing an exception.
        Integer missingScore = studentScores.get("George");

        System.out.println("Looking up George:");
        System.out.println("Result: " + missingScore);

        // Edge Case 2: Safely checking whether a key exists
        // before attempting to remove it.
        System.out.println("\nAttempting to delete George:");

        if (studentScores.containsKey("George")) {
            studentScores.remove("George");
            System.out.println("George was deleted.");
        } else {
            System.out.println(
                    "George was not found, so nothing was deleted."
            );
        }

        // Edge Case 3: Adding a key that does not exist.
        // This creates a new key-value pair.
        studentScores.put("George", 82);

        System.out.println("\nAfter adding George as a new key:");
        System.out.println(studentScores);

        // ===============================
        // CHECKING FOR A KEY
        // ===============================

        System.out.println("\n=== KEY SEARCH ===");

        if (studentScores.containsKey("Alice")) {
            System.out.println("Alice exists in the HashMap.");
        }

        if (!studentScores.containsKey("Henry")) {
            System.out.println("Henry does not exist in the HashMap.");
        }

        // ===============================
        // PROGRAM COMPLETE
        // ===============================

        System.out.println("\n=== PROGRAM COMPLETE ===");
    }
}
