"""
This program creates a Binary Search Tree Vertex and a Binary Search Tree. It also computes the average height of a binary tree for different n-values.
"""

import random
import math

# Binary Search Tree (BST) Implementation

class BSTVertex:
    def __init__(self, key):
        # Initialize a vertex (node) in the Binary Search Tree
        self.key = key  # The value (key) of the vertex
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree
        self.root = None

    def insert(self, x):
        # Public method to insert a value into the BST
        self.root = self._insert(self.root, x)

    def _insert(self, root, x):
        # Recursive helper method to insert a value into the BST
        if root is None:
            return BSTVertex(x)  # Create a new vertex if the current root is None
        if x < root.key:
            root.left = self._insert(root.left, x)  # Insert into the left subtree if x is smaller
        else:
            root.right = self._insert(root.right, x)  # Insert into the right subtree if x is larger
        return root

    def height(self):
        # Public method to calculate the height of the BST
        return self._height(self.root)

    def _height(self, root):
        # Recursive helper method to calculate the height of the BST
        if root is None:
            return 0  # A null tree has a height of 0
        else:
            left_height = self._height(root.left)  # Calculate height of left subtree
            right_height = self._height(root.right)  # Calculate height of right subtree
            return 1 + max(left_height, right_height)  # Return the larger height + 1 (for the root)

    def total_height(self):
        # Public method to calculate the total height (sum of depths of all nodes) in the BST
        return self._total_height(self.root, 0)

    def _total_height(self, root, depth):
        # Recursive helper method to calculate the total height of the BST
        if root is None:
            return 0  # No contribution to height if the subtree is null

        left_height = self._total_height(root.left, depth + 1)  # Calculate for the left subtree
        right_height = self._total_height(root.right, depth + 1)  # Calculate for the right subtree

        return depth + left_height + right_height  # Sum the depths and return

# Experiment with given series with 500 trials

def generate_random_permutation(n):
    # Generate a random permutation of integers from 1 to n
    return random.sample(range(1, n + 1), n)

def average_height_experiment(n, num_trials):
    # Perform an experiment to calculate the average height of a BST for a given n over multiple trials
    total_height_sum = 0  # Initialize the sum of all heights

    for _ in range(num_trials):
        # For each trial, generate a random permutation and build a BST
        permutation = generate_random_permutation(n)  # Generate a random permutation of size n
        bst = BST()  # Create a new Binary Search Tree

        for value in permutation:
            bst.insert(value)  # Insert all values of the permutation into the BST

        total_height_sum += bst.height()  # Add the height of the BST to the total sum

    # Calculate and return the average height
    average_height = total_height_sum / num_trials
    return average_height

# Perform experiments for various values of n
n_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  # List of n-values to test
num_trials = 500  # Number of trials for each n

# Collect experimental data
average_heights = [average_height_experiment(n, num_trials) for n in n_values]  # Average heights for all n-values
print("Average Heights:", average_heights)

# Hypotheses

# Hypothesis 1: The average height can be approximated by c * n
# For each n, calculate c as average_height / n
H1 = [average_height / n for average_height, n in zip(average_heights, n_values)]
print("Hypothesis 1:", H1)

# Hypothesis 2: The average height can be approximated by c * log(n)
# For each n, calculate c as average_height / log(n)
H2 = [average_height / math.log(n) for average_height, n in zip(average_heights, n_values)]
print("Hypothesis 2:", H2)
