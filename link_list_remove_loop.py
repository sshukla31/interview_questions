'''
Find and remove loop LinkList
'''



from commons.link_list import LinkList



def resolve_loop(head):
    # 1) check if loop exists
    is_loop = False
    pointer_i = pointer_j = head

    while(pointer_j != None):
        pointer_i = pointer_i.next
        try:
            pointer_j = pointer_j.next.next
        except:
            pointer_j = pointer_j.next

        if pointer_i == pointer_j:
            print "Loop present. Pointers collide at value: {}".format(pointer_i.data)
            is_loop = True
            break

    if not is_loop:
        return is_loop

    # 2) now find the start of the loop
    pointer_i = head

    while(pointer_i != pointer_j):
        pointer_i = pointer_i.next
        pointer_j = pointer_j.next

    print "Loop begins at: {}".format(pointer_j.data)

    # 3) now resolve loop
    while(pointer_i.next != pointer_j):
        pointer_i = pointer_i.next

    pointer_i.next = None
    print "Loop resolved by adding None to last node: {}".format(pointer_i.data)


if __name__ == '__main__':
    ll = LinkList()
    for val in [8, 1, 9, 4, 2, 3, 7, 5, 6]:
        ll.add(val)

    # Create a loop
    node1 = ll.get_node(2)

    ll.tail.next = node1

    resolve_loop(ll.head)

    print ll.print_result()