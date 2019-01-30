from LinkedList import Node

def mergeSortedLinkedLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.data > l2.data:
        l2.next = mergeSortedLinkedLists(l1, l2.next)
        return l2
    else:
        l1.next = mergeSortedLinkedLists(l1.next, l2)
        return l1

def test():
    n1 = Node(3)
    n1.next = Node(7)
    n1.next.next = Node(8)
    n1.next.next.next = Node(10)
    n1.next.next.next.next = Node(15)
    n1.printList()

    n2 = Node(1)
    n2.next = Node(2)
    n2.next.next = Node(10)
    n2.next.next.next = Node(11)
    n2.printList()

    n3 = mergeSortedLinkedLists(n1, n2)
    n3.printList()

# test()
