"""
Priority Queue ADT/ HEAP / HEAP SORT
Statement:
  Given a disordered list of integers (or any other items),
  rearrange the integers in order of max/min

  Sample Input: [8,5,3,1,9,6,0,7,4,2,5]
  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
"""

class BinaryHeap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_size(self):
        return self.size

    def parent(self, index):
        return (index - 1)/2

    def left_children(self, index):
        return (2 * index) + 1

    def right_children(self, index):
        return (2 * index) + 2

    def parent_val(self, index):
        try:
            return self.heap[(index - 1)/2]
        except IndexError:
            return None

    def left_children_val(self, index):
        try:
            return self.heap[(2 * index) + 1]
        except IndexError:
            return None

    def right_children_val(self, index):
        try:
            return self.heap[(2 * index) + 2]
        except IndexError:
            return None

    def get_max(self):
        return -1 if self.size == 0 else self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.size = len(self.heap) - 1
        self.percolate_up(self.size)

    def percolate_up(self, index):
        while(self.parent(index) >= 0):
            parent_index = self.parent(index)
            if self.heap[index] > self.heap[parent_index]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[parent_index]
                self.heap[parent_index] = tmp

            index = parent_index

    def delete_max(self):
        if self.size == 0:
            return -1
        elif self.size == 1:
            self.heap.pop()
        elif self.size == 2:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
        else:
            # we can simply assign heap[0] = heap[-1] and pop()
            # but here we follow regular step
            tmp = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap[-1] = tmp

            self.heap.pop()

            self.heapify()


        self.size = len(self.heap)

    def build_max_heap(self, array):
        self.size = len(array) - 1
        self.heap = array
        index = (self.size - 1) / 2
        while(index >= 0):
            print self.heap
            self.percolate_down(index)
            index -= 1

    def percolate_down(self, index):
        # check if atleast one child exists. Hence, we check for left child.
        has_child = lambda index: True if self.left_children(index) < self.size else False
        while(has_child(index)):
            max_child = self.max_child(index)
            if self.heap[index] < self.heap[max_child]:
                tmp = self.heap[max_child]
                self.heap[max_child] = self.heap[index]
                self.heap[index] = tmp

            index = max_child

    def max_child(self, index):
        if self.right_children(index) > self.size:
            # 'has_child' confirms already that left_child exists.Hence, to avoid IndexError
            # we check if right child also exists, else, we return left child
            return self.left_children(index)
        elif self.left_children_val(index) > self.right_children_val(index):
            return self.left_children(index)
        else:
            return self.right_children(index)


    #def heapify(self, elements=None):
    #    elements = elements if elements else self.heap
    #    start = (len(elements) - 1) / 2
    #    for index in range(start , -1 , -1):
    #        parent_index = self.parent(index)
    #        if elements[parent_index] < elements[index]:
    #            tmp = elements[index]
    #            elements[index] = elements[parent_index]
    #            elements[parent_index] = tmp

    #def sort(self, unsorted_elements):
    #    pass


if __name__ == '__main__':
    array = [8,5,3,1,9,6,0,7,4,2,5]
    binary_heap = BinaryHeap()
    expected_heap = [9, 8, 6, 7, 5, 3, 0, 1, 4, 2, 5]
    print "################"
    print "#  BUILD HEAP  #"
    print "################"
    binary_heap.build_max_heap(array=array)
    actual_heap = binary_heap.heap
    print binary_heap.heap
    assert actual_heap == expected_heap

    print "\n################"
    print "#  INSERT HEAP #"
    print "################\n"
    for val in [10, 11]:
        print "Insert:{}".format(val)
        binary_heap.insert(val)
        print binary_heap.heap

    actual_heap = binary_heap.heap
    expected_heap = [11, 8, 10, 7, 5, 9, 0, 1, 4, 2, 5, 3, 6]
    assert actual_heap == expected_heap