"""
This program increases the size of a stack when needed, and converts recursive functions into non-recursive functions by using stacks.
"""

# Stack Implementation
class Stack:
    def __init__(self):
        # Initialize an empty stack with a 10-element array
        self.stack_array = [None] * 10  # Predefined size of 10
        self.top = -1  # Pointer to the top of the stack

    def is_empty(self):
        # Check if the stack is empty
        return self.top == -1

    def push(self, item):
        # Push an element onto the stack
        if self.top == len(self.stack_array) - 1:
            # Resize the stack if it is full
            new_size = 2 * len(self.stack_array)  # Double the size of the stack
            new_stack_array = [None] * new_size  # Create a new larger array
            # Copy all elements from the old array to the new one
            for i in range(len(self.stack_array)):
                new_stack_array[i] = self.stack_array[i]
            self.stack_array = new_stack_array  # Replace old array with the new one
        self.top += 1  # Increment the top index
        self.stack_array[self.top] = item  # Add the new item

    def pop(self):
        # Remove and return the top element from the stack
        if self.is_empty():
            print("Stack Underflow: Cannot pop from an empty stack.")
            return None
        else:
            popped_item = self.stack_array[self.top]  # Get the top element
            self.top -= 1  # Decrement the top index
            return popped_item  # Return the popped element

# Collatz-like sequence

def F1(n):
    # Recursive implementation of the Collatz sequence
    if n > 1:
        if n % 2 == 0:
            F1(n // 2)  # For even numbers, divide by 2
        else:
            F1(3 * n + 1)  # For odd numbers, apply 3n + 1
    print(n)  # Print the current value

def non_recursive_F1(n):
    # Non-recursive implementation of the Collatz sequence using a stack
    stack = Stack()  # Initialize a stack
    stack.push(n)  # Push the starting value onto the stack
    current = n

    # Generate the Collatz sequence
    while current > 1:
        if current % 2 == 0:
            current = current // 2  # Even case
        else:
            current = 3 * current + 1  # Odd case
        stack.push(current)  # Push each new value onto the stack

    # Print the sequence in reverse order by popping from the stack
    while not stack.is_empty():
        print(stack.pop())

# Function with recursive calls

def F2(n):
    # Recursive function
    if n >= 6:
        F2(n % 3)  # First recursive call with modulo
        F2(2 * n // 3)  # Second recursive call with integer division
    print(n)

def non_recursive_F2(n):
    # Non-recursive version using stacks
    stack = Stack()  # Stack for processing elements
    stack1 = Stack()  # Stack for storing the result in reverse order

    stack.push(n)  # Push the initial value onto the first stack

    # Process the stack until empty
    while not stack.is_empty():
        current = stack.pop()  # Pop an element
        stack1.push(current)  # Push it onto the second stack

        # If the condition is met, push the next values onto the first stack
        if current >= 6:
            stack.push(current % 3)
            stack.push(2 * current // 3)

    # Print the reversed result by popping from the second stack
    while not stack1.is_empty():
        print(stack1.pop())

# Midpoint function

def F3(a, b):
    # Recursive midpoint function
    if a <= b:
        m = (a + b) // 2  # Calculate the midpoint
        F3(a, m - 1)  # Recursive call for the left half
        print(m)  # Print the midpoint
        F3(m + 1, b)  # Recursive call for the right half

def non_recursive_F3(a, b):
    # Non-recursive midpoint function using a stack
    if a > b:
        a, b = b, a  # Ensure a <= b

    mstack = Stack()  # Auxiliary stack for midpoints
    S = Stack()  # Main stack for ranges
    S.push((a, b))  # Push the initial range onto the stack

    while not S.is_empty():
        currA, currB = S.pop()  # Pop the current range

        if currA <= currB:
            m = (currA + currB) // 2  # Calculate the midpoint
            S.push((m + 1, currB))  # Push the right range
            S.push((currA, m - 1))  # Push the left range
            mstack.push(m)  # Store the midpoint

    # Print the midpoints in the correct order
    while not mstack.is_empty():
        print(mstack.pop())

# Another midpoint function with a different order

def F4(a, b):
    # Recursive midpoint function
    if a <= b:
        m = (a + b) // 2  # Calculate the midpoint
        F4(a, m - 1)  # Recursive call for the left half
        F4(m + 1, b)  # Recursive call for the right half
        print(m)  # Print the midpoint

def non_recursive_F4(a, b):
    # Non-recursive midpoint function using stacks
    os = Stack()  # Stack for ranges
    rs = Stack()  # Stack for results
    os.push((a, b))  # Push the initial range onto the stack

    while not os.is_empty():
        currA, currB = os.pop()  # Pop the current range

        if currA <= currB:
            m = (currA + currB) // 2  # Calculate the midpoint
            rs.push(m)  # Push the midpoint onto the result stack
            os.push((currA, m - 1))  # Push the left range
            os.push((m + 1, currB))  # Push the right range

    # Print the results in reverse order
    while not rs.is_empty():
        print(rs.pop())

# Main function to test all implementations
def main():
    print("Name: Rahul Kumar")

    # Test F1 and its non-recursive version
    for i in [7, 18, 19, 22, 105]:
        print(f"Function F1 with number {i}")
        print("Recursive Function F1:")
        F1(i)
        print("Non-Recursive F1:")
        non_recursive_F1(i)

    # Test F2 and its non-recursive version
    for i in [7, 18, 19, 22, 43]:
        print(f"Function F2 with number {i}")
        print("Recursive Function F2:")
        F2(i)
        print("Non-Recursive F2:")
        non_recursive_F2(i)

    # Test F3 and its non-recursive version
    f3listandf4list = [(0, 7), (1, 18), (4, 19), (-1, 22)]
    for x in f3listandf4list:
        print(f"Function F3 with range {x}")
        print("Recursive Function F3:")
        F3(x[0], x[1])
        print("Non-Recursive F3:")
        non_recursive_F3(x[0], x[1])

    # Test F4 and its non-recursive version
    for x in f3listandf4list:
        print(f"Function F4 with range {x}")
        print("Recursive Function F4:")
        F4(x[0], x[1])
        print("Non-Recursive F4:")
        non_recursive_F4(x[0], x[1])

# Run the main function
if __name__ == "__main__":
    main()
