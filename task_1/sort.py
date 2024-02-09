def merge_sort_linked_list(head):
    """
    Sorts a linked list using the merge sort algorithm.

    :param head: The head node of the linked list.
    :return: The head node of the sorted linked list.
    """
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


def get_middle(head):
    """
    Get the middle node of a linked list.

    :param head: The head node of the linked list.
    :return: The middle node of the linked list.
    """
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def sorted_merge(a, b):
    """
    Merges two sorted linked lists and returns the merged list.

    :param a: The head node of the first sorted linked list.
    :param b: The head node of the second sorted linked list.
    :return: The head node of the merged sorted linked list.
    """
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result
