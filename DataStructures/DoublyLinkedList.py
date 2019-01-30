class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.data)

    def printList(self, reversed=False):
        print(self)
        if reversed:
            if self.prev:
                self.prev.printList(reversed)
        else:
            if self.next:
                self.next.printList()

def test():
    n1 = Node(5)
    n1.next = Node(4, n1)
    n1.next.next = Node(1, n1.next)
    n1.next.next.next = Node(7, n1.next.next)

    n1.printList()
    n1.next.next.next.printList(reversed=True)

    while n1:
        if n1.prev:
            print("The last node's data is: " + str(n1.prev))
        else:
            print("This is the first node")
        print("This node's data is: " + str(n1))
        if n1.next:
            print("The next node's data is: " + str(n1.next))
        else:
            print("This is the last node")
        n1 = n1.next

# test()
