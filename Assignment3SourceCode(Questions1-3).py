"""
This program explores quadratic probing and double hashing by determining a table size that lets you achieve the required performance standard.
"""

import string
import random

class HashTable:
    def __init__(self, ts, method, c1=None, c2=None, dc1=None, dc2=None):
        """
        Initialize the HashTable with:
        - ts: table size
        - method: hashing method ("quadratic" or "double")
        - c1, c2: constants for quadratic probing
        - dc1, dc2: constants for double hashing
        """
        self.ts = ts  # Table size
        self.hs = [None] * ts  # Hash table initialized with None
        self.method = method  # Hashing method: "quadratic" or "double"
        self.c1 = c1  # Coefficient for linear term in quadratic probing
        self.c2 = c2  # Coefficient for quadratic term in quadratic probing
        self.dc1 = dc1  # Coefficient for the primary term in double hashing
        self.dc2 = dc2  # Coefficient for the secondary hash function
        self.tcomp = 0  # Track total comparisons made during insertions

    def primary_hash(self, key):
        """
        Primary hash function:
        Computes the hash value of a key using a simple positional-weighted sum formula.
        """
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += (ord(char) * (i + 1))  # Weighted sum of ASCII values of characters
        return hash_value % self.ts  # Modulo operation to fit into table size

    def quadratic_probe(self, key, attempt):
        """
        Quadratic probing:
        Computes the next index to probe using the quadratic probing formula.
        """
        if self.method == "quadratic":
            return (self.primary_hash(key) + self.c1 * attempt + self.c2 * attempt ** 2) % self.ts
        return 0

    def secondary_hash(self, key):
        """
        Secondary hash function:
        Computes a secondary hash value for double hashing.
        """
        hash_value = 0
        for char in key:
            hash_value = (hash_value * self.dc2 + ord(char)) % (self.ts - 1)  # Hash calculation
        return hash_value + 1  # Ensures the secondary hash value is never zero

    def double_hash(self, key, attempt):
        """
        Double hashing:
        Computes the next index to probe using double hashing formula.
        """
        if self.method == "double":
            return (self.primary_hash(key) + attempt * self.secondary_hash(key)) % self.ts
        return 0

    def insert(self, key):
        """
        Inserts a key into the hash table using either quadratic probing or double hashing.
        """
        for attempt in range(self.ts):  # Attempt probing up to table size
            self.tcomp += 1  # Increment total comparisons
            index = self.quadratic_probe(key, attempt) if self.method == "quadratic" else self.double_hash(key, attempt)
            if self.hs[index] is None:  # If the index is empty, insert the key
                self.hs[index] = key
                return True
        return False  # If the table is full, insertion fails

    def average_comparisons(self):
        """
        Computes the average number of comparisons per insertion.
        """
        return self.tcomp / self.ts  # Average comparisons over total table size

def generate_codewords(n, lengths=[7, 8]):
    """
    Generates a set of unique codewords consisting of random letters of specified lengths.
    - n: number of codewords to generate
    - lengths: list of possible lengths for the codewords
    """
    codewords = set()
    while len(codewords) < n:  # Continue until the desired number of unique codewords is generated
        length = random.choice(lengths)  # Choose a random length
        codeword = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))  # Generate a random string
        codewords.add(codeword)  # Add the codeword to the set
    return list(codewords)  # Convert the set to a list for further use

def get_user_input():
    """
    Gets user input for:
    - Table size (ts)
    - Hashing method (quadratic probing or double hashing)
    - Relevant constants for the chosen method
    """
    print("\nEnter ts (table size) (or 0 to exit): ")
    ts = int(input())  # Input table size
    if ts == 0:  # Exit condition
        return ts, None, None, None, None, None

    print("Select hash method:")
    print("1. Quadratic Probing")
    print("2. Double Hashing")
    method_choice = input("Enter choice (1/2): ")  # Choose the hashing method
    method = "quadratic" if method_choice == '1' else "double"

    if method == "quadratic":  # Input constants for quadratic probing
        c1 = int(input("Enter value for c1: "))
        c2 = int(input("Enter value for c2: "))
        return ts, method, c1, c2, None, None
    else:  # Input constants for double hashing
        dc1 = int(input("Enter value for dc1: "))
        dc2 = int(input("Enter value for dc2: "))
        return ts, method, None, None, dc1, dc2

def simulate():
    """
    Simulates the hash table insertion process and calculates the average comparisons per insertion.
    """
    while True:
        ts, method, c1, c2, dc1, dc2 = get_user_input()  # Get user input
        if ts == 0:  # Exit if table size is 0
            break

        # Initialize the hash table
        hash_table = HashTable(ts, method, c1, c2, dc1, dc2)
        # Generate 2000 unique random codewords
        codewords = generate_codewords(2000)

        # Insert each codeword into the hash table
        for codeword in codewords:
            hash_table.insert(codeword)

        # Display results
        print(f"Method: {method.title()} Hashing")
        print(f"Average comparisons per insertion: {hash_table.average_comparisons():.2f}")

# Run the simulation
if __name__ == "__main__":
    simulate()

