class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    # Push an item onto the stack
    def push(self, n):
        self.stack.append(n)
        return self.stack

    # Remove and return the top item from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    # Return the top item without removing it
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    # Helper: Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Helper: Get the size of the stack
    def size(self):
        return len(self.stack)

    # Clean representation for easy debugging
    def __repr__(self):
        return f"Stack(size={self.size()}, top={self.peek() if not self.is_empty() else None}, elements={self.stack})"




if __name__ == "__main__":
    print("=== Testing Stack ===")
    stack = Stack()
    
    # Test push
    print("Initial State:")
    print(stack.push(1))
    stack.push(2)
    print("After pushing 2 and 3:")
    print(stack.push(3))

    # Test peek
    print("\n--- Testing peek ---")
    print(f"Top element: {stack.peek()}")  # Should be 3
    print(stack)

    # Test pop
    print("\n--- Testing pop ---")
    print(f"Popped: {stack.pop()}")  # Should be 3
    print("After pop:")
    print(stack)

    # Test empty check
    print(f"Is stack empty? {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")
