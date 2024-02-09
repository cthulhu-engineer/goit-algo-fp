class Node:
    """
    Node class represents a node in a linked list.

    :param data: The data to be stored in the node (default is None).
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    LinkedList

    A class representing a linked list data structure.

    Methods:
        - __init__
        - append
        - print_list

    Attributes:
        - head

    """
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
