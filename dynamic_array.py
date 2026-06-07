# Python arrays are dynamic by default, but this is an example of resizing.

class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * self.capacity

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        # insert at the next empty position
        self.arr[self.length] = n
        self.length += 1
   
    def resize(self):
        # create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        
        self.arr = newArr

    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1
            # Optional: clear the element to avoid loitering
            self.arr[self.length] = 0

    # Get value at index i
    def get(self, i):
        if 0 <= i < self.length:
            return self.arr[i]
        raise IndexError("Index out of bounds")

    # Insert n at i-th index
    def insert(self, i, n):
        # 1. Bounds check: Can insert from index 0 up to self.length (inclusive)
        if i < 0 or i > self.length:
            raise IndexError("Index out of bounds")
        
        # 2. Resize if the array is full
        if self.length == self.capacity:
            self.resize()
            
        # 3. Shift elements to the right to make room
        for j in range(self.length, i, -1):
            self.arr[j] = self.arr[j - 1]
            
        # 4. Insert the new element and increment length
        self.arr[i] = n
        self.length += 1

    # Helper to easily print the array elements
    def __repr__(self):
        return f"Array(length={self.length}, capacity={self.capacity}, elements={self.arr[:self.length]})"


if __name__ == "__main__":
    print("=== Testing Dynamic Array ===")
    
    # 1. Initialize array (starts with capacity 2)
    arr = Array()
    print("Initial state:")
    print(arr)  # Should show length=0, capacity=2

    # 2. Test pushback and auto-resize
    print("\n--- Testing pushback and resizing ---")
    arr.pushback(10)
    arr.pushback(20)
    print("After 2 pushbacks (at capacity):")
    print(arr)  # Should show length=2, capacity=2

    arr.pushback(30)
    print("After 3rd pushback (triggers resize to capacity 4):")
    print(arr)  # Should show length=3, capacity=4

    # 3. Test insert (with shifting)
    print("\n--- Testing insert ---")
    arr.insert(1, 15)
    print("After inserting 15 at index 1:")
    print(arr)  # Should show length=4, capacity=4, elements=[10, 15, 20, 30]

    # 4. Test get
    print("\n--- Testing get ---")
    try:
        print(f"Element at index 1: {arr.get(1)}")  # Should print 15
        print(f"Element at index 3: {arr.get(3)}")  # Should print 30
        print("Attempting to get out-of-bounds index 10...")
        arr.get(10)
    except IndexError as e:
        print(f"Caught expected error: {e}")

    # 5. Test popback
    print("\n--- Testing popback ---")
    arr.popback()
    print("After popback (should remove 30):")
    print(arr)  # Should show length=3, capacity=4

