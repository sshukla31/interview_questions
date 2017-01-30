"""
Graph: Check if cycle exists in the graph

Algorithm:
    1) Apply DFS
    2) If adjacent node exists in the graph,
       1) If adjacent node == parent, then continue
       2) If adjacent node != parent, then loop exists
"""


from sets import Set

from commons.stack import Stack


class Node(object):
    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors else []

    def __repr__(self):
        return self.value


class UndirectedGraph(object):
    def __init__(self):
        pass

    def is_cycle(self, start):
        # run DFS. Alongwith DFS, for current node pass last node via which
        # we reached current node. eg: A -> B. So, if we reach B from A,
        # pass 'A' to 'B' so that 'B' doesn't take path to 'A' but try' other
        # neighbors
        no_cycle_found = True
        visited = Set([])
        stack = Stack()
        stack.push((start, None))  # node, parent
        result = (False, None, None) # found cycle, start, cycle

        while(stack.is_empty() == False and no_cycle_found is True):
            node, parent = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in node.neighbors:
                    if neighbor == parent:
                        # if neighbor already in visited but parent then
                        # don't follow that route
                        continue
                    elif neighbor in visited:
                        # if neighbor already in visited and not parent then
                        # it means there are more than 1 ways to reach same neighbor
                        # Hence, cycle exits
                        no_cycle_found = False
                        print "Cycle Found between: {} -> {}".format(node.value, neighbor.value)
                        result = (True, node, neighbor)
                        break
                    else:
                        stack.push((neighbor, node)) # node, adjacent_node

                    # else:
                    #    if neighbor != adjacent_node:
                    #        print "Cycle Found between- {}:{}".format(node.value, neighbor.value)


        return result


nodeF = Node('f')
nodeB = Node('b')
nodeD = Node('d')
nodeE = Node('e')
nodeC = Node('c', [nodeB, nodeD])
nodeA = Node('a', [nodeB, nodeF])
nodeB.neighbors = [nodeA, nodeC, nodeE]
nodeE.neighbors = [nodeB, nodeD]
nodeD.neighbors = [nodeC, nodeE]
nodeF.neighbors = [nodeA]


if __name__ == '__main__':
    ug = UndirectedGraph()

    # Test when loop exists
    actual_result = ug.is_cycle(nodeA)
    expected_result = (True, nodeC, nodeB)
    assert actual_result == expected_result


    # Test when loop doesn't exists
    # Remove connection between nodeB and nodeE
    nodeB.neighbors = [nodeA, nodeC]
    nodeE.neighbors = [nodeD]
    actual_result = ug.is_cycle(nodeA)
    expected_result = (False, None, None)

