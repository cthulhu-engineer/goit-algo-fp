from task_1.linked_list_impl import Node


def merge_sorted_lists(a, b):
    """
    Merges two sorted linked lists in ascending order and returns the merged list.

    :param a: The head node of the first linked list.
    :param b: The head node of the second linked list.
    :return: The head node of the merged linked list.
    """
    dummy = Node()
    tail = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return dummy.next
