
# first 2 steps
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None


    def append(self,data):
        newNode=Node(data)
        if self.head == None:
            self.head=newNode
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=newNode
    
    def print_list(self):
        ptr=self.head
        while ptr:
            print(ptr.data,"",end=" -> ")
            ptr=ptr.next
        print("None")

li1=LinkedList()

li1.append(10)
li1.append(9)
li1.append(11)
li1.append(10)

li1.print_list()


