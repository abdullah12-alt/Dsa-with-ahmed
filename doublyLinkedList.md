 A doubly linked list is a type of linked list where each node contains a reference to both the next and the previous node in the sequence. This allows for more efficient traversal in both directions compared to a singly linked list.

Here's a step-by-step guide to creating a doubly linked list in Python:

### Step 1: Define the Node Class
First, we'll define a `Node` class to represent each element in the list. Each node will have three attributes: `data` to store the value, `next` to store the reference to the next node, and `prev` to store the reference to the previous node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

### Step 2: Define the Doubly Linked List Class
Next, we'll define the `DoublyLinkedList` class to manage the list. This class will have methods to insert, delete, and display nodes.

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        if self.head is None:
            return
        curr_node = self.head
        while curr_node and curr_node.data != key:
            curr_node = curr_node.next
        if curr_node is None:
            return
        if curr_node.prev:
            curr_node.prev.next = curr_node.next
        if curr_node.next:
            curr_node.next.prev = curr_node.prev
        if curr_node == self.head:
            self.head = curr_node.next
        curr_node = None
    
    def display(self):
        nodes = []
        curr_node = self.head
        while curr_node:
            nodes.append(curr_node.data)
            curr_node = curr_node.next
        print("Doubly Linked List:", nodes)
```

### Step 3: Using the Doubly Linked List
Now, we can create an instance of `DoublyLinkedList` and use its methods to manipulate the list.

```python
# Create a doubly linked list
dll = DoublyLinkedList()

# Append elements to the list
dll.append(1)
dll.append(2)
dll.append(3)

# Display the list
dll.display()  # Output: Doubly Linked List: [1, 2, 3]

# Prepend elements to the list
dll.prepend(0)
dll.display()  # Output: Doubly Linked List: [0, 1, 2, 3]

# Delete an element from the list
dll.delete(2)
dll.display()  # Output: Doubly Linked List: [0, 1, 3]
```

### Explanation:
1. **Node Class**: Each node has a `data` attribute to store the value, and `next` and `prev` attributes to point to the next and previous nodes, respectively.
2. **DoublyLinkedList Class**: 
   - The `append` method adds a node to the end of the list.
   - The `prepend` method adds a node to the beginning of the list.
   - The `delete` method removes a node with the specified value from the list.
   - The `display` method prints the elements of the list.

