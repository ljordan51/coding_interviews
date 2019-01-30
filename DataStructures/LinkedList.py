class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

    def printList(self):
        print(self)
        if self.next:
            self.next.printList()


def test():
    n1 = Node(7)
    print(n1.next)
    n1 = Node(7, Node(3))
    print(n1.next)
    n1.next = Node(5)
    print(n1.next)
    n1.next.next = Node(8)
    n1.next.next.next = Node(10)
    n1.next.next.next.next = Node(1)

    n1.printList()

    while n1:
        print(n1)
        n1 = n1.next

# test()
