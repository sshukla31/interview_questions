'''
Implement an algorithm to find the kth to last element of a linked list.

  4->3->1->5->6->7->8

  k=1, output=7
  k=2, output=6

  Solution:
  1) Create k distance between pointer and end of the node
  2) To create a distance, define an extra pointer and move k distance from
     the first pointer

  Steps:
    1) Create 2 pointers and point to head node, say i and j
    2) Move pointer j by k positions
    3) Move pointer i and j one by one until j reaches end of the node
    4) Print value at pointer i


'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.tail
            temp.next = self.tail = new_node

    def find_kth_to_last_element(self, k):
        if any([
            k is None,
            isinstance(k, int) == False,
            k < 0
        ]):
            return "Invalid value k: {}".format(k)

        i = j = self.head
        while(k > 0):
            j = j.next
            k = k - 1

        while(j.next != None):
            i = i.next
            j = j.next

        return i.data


if __name__ == '__main__':
    link_list = LinkList()
    for val in [4, 3, 1, 5, 6, 7, 8]:
        link_list.add(val)

    link_list.find_kth_to_last_element(k=1)
    link_list.find_kth_to_last_element(k=2)
    link_list.find_kth_to_last_element(k='a')
    link_list.find_kth_to_last_element(k=None)
    link_list.find_kth_to_last_element(k=-1)