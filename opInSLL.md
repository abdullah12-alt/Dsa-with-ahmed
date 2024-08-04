

### Singly Linked List in Python

A **singly linked list** is a data structure that consists of a sequence of nodes, each containing data and a reference (or a link) to the next node in the sequence. It allows for efficient insertion and deletion of elements.

#### Basic Structure

1. **Node**: Each node in the linked list contains two parts:
   - **Data**: Stores the value.
   - **Next**: A reference to the next node in the list.

2. **Linked List**: The linked list itself only needs a reference to the first node, often called the **head**.

#### Node Class

First, we define a `Node` class:

```python
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next node as None
```

#### LinkedList Class

Next, we define a `LinkedList` class to manage the nodes:

```python
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def is_empty(self):
        return self.head is None  # Check if the list is empty

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.is_empty():
            self.head = new_node  # If the list is empty, set the new node as the head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end

    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Set the new node's next to the current head
        self.head = new_node  # Set the new node as the head of the list

    def delete_with_value(self, data):
        if self.is_empty():
            return  # If the list is empty, do nothing

        if self.head.data == data:
            self.head = self.head.next  # If the head node is to be deleted, move the head to the next node
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Bypass the node to be deleted
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  # Return True if the data is found
            current = current.next
        return False  # Return False if the data is not found

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)  # Collect data of each node
            current = current.next
        print(" -> ".join(map(str, elements)))  # Display the list in a readable format
```

#### Usage Example

Let's create a linked list and perform some operations:

```python
# Create a new linked list
linked_list = LinkedList()

# Append elements
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Display the list
print("Initial list:")
linked_list.display()

# Prepend an element
linked_list.prepend(0)

# Display the list again
print("After prepending 0:")
linked_list.display()

# Delete an element
linked_list.delete_with_value(2)

# Display the list again
print("After deleting 2:")
linked_list.display()

# Find an element
print("Is 3 in the list?")
print(linked_list.find(3))

print("Is 2 in the list?")
print(linked_list.find(2))
```

Output:
```
Initial list:
1 -> 2 -> 3
After prepending 0:
0 -> 1 -> 2 -> 3
After deleting 2:
0 -> 1 -> 3
Is 3 in the list?
True
Is 2 in the list?
False
```

### Explanation of Methods

1. **append(data)**: Adds a new node with the specified data at the end of the list.
2. **prepend(data)**: Adds a new node with the specified data at the beginning of the list.
3. **delete_with_value(data)**: Removes the first node that contains the specified data.
4. **find(data)**: Checks if a node with the specified data exists in the list.
5. **display()**: Prints out the elements of the list in a readable format.
