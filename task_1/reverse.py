def reverse_linked_list(linked_list):
    """
    Reverses a linked list by modifying the next pointers of each node.

    :param linked_list: The linked list to be reversed.
    :return: None
    """
    prev = None
    current = linked_list.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev
