class Node:
    def __init__(self,date=None):
        self.data=date
        self.next=None
        self.prev=None



class DoublyList:
    def __init__(self):
         self.head=None
    
    def append(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return
        last_node=self.head

        while last_node.next:
            last_node=last_node.next
        last_node.next=new_Node
        new_Node.prev=last_node

    def traversal(self):
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next




dbl=DoublyList()
dbl.append(2)
dbl.append(5)
dbl.append(9)
dbl.append(10)
dbl.append(11)
dbl.traversal()