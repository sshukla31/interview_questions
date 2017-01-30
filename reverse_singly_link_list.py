'''
Reverse Singly Link List

Algorithm:
    1) Create a temporary variable last and current
    2) Assign current to head and last = None
    3) Loop through end of the link list
        new_node = current node
        current = current.next
        new_node.next = last
        last = new_node
'''

from commons.link_list import LinkList


def reverse_link_list(head):
    """
    Reverse a singly link list given head
    """
    if head is None:
        return head

    last = None
    current = head

    while(current != None):
        new_node = current
        current = current.next
        new_node.next = last
        last = new_node

    return last


if __name__ == '__main__':
    ll = LinkList()
    elements = [1, 2, 3, 4]
    for val in elements:
        ll.add(val)

    reverse_list = reverse_link_list(ll.head)
    expected_result = elements[::-1]
    actual_result = []
    while(reverse_list != None):
        actual_result.append(reverse_list.data)
        reverse_list = reverse_list.next

    assert expected_result == actual_result

