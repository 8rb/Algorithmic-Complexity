class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printy(self):
        val = self.head
        while val != None:
            print(val.data)
            val = val.next
    
    def append(self, node):
        val = self.head
        while val.next != None:
            val = val.next
        val.next = node


listy = LinkedList()
listy.head = Node(1)

second = Node(2)
third = Node(3)
fourth = Node(4)
listy.append(second)
listy.append(third)
listy.append(fourth)

listy.printy()