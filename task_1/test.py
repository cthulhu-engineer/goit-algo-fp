from task_1.linked_list_impl import LinkedList
from task_1.merge import merge_sorted_lists
from task_1.reverse import reverse_linked_list
from task_1.sort import merge_sort_linked_list

if __name__ == '__main__':
    # Створення та наповнення однозв'язних списків
    ll = LinkedList()
    for i in range(10, 0, -1):
        ll.append(i)
    print("Оригінальний список:")
    ll.print_list()

    # Реверсування списку
    reverse_linked_list(ll)
    print("Реверсований список:")
    ll.print_list()

    # Сортування списку злиттям
    ll.head = merge_sort_linked_list(ll.head)
    print("Відсортований список:")
    ll.print_list()

    # Створення та наповнення другого відсортованого списку
    ll2 = LinkedList()
    for i in range(15, 10, -1):
        ll2.append(i)
    ll2.head = merge_sort_linked_list(ll2.head)

    # Об'єднання двох відсортованих списків
    merged_list_head = merge_sorted_lists(ll.head, ll2.head)
    print("Об'єднаний відсортований список:")
    current = merged_list_head
    while current:
        print(current.data, end=' -> ')
        current = current.next
    print('None')
