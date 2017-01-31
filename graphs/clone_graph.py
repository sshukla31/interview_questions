'''
Clone a Graph or create a deepcopy of a Graph
Each node has neighbors


               /----A
              /   /   \
               B        C
             /   \
           D       E

'''


class Node(object):
    def __init__(self, neighbors=None):
        self.neighbors = neighbors if neighbors else []


nodeD = Node()
nodeE = Node()
nodeB = Node()
nodeC = Node()
nodeA = Node([nodeB, nodeC])
nodeB.neighbors = [nodeA, nodeD, nodeE]



def deepcopy(node, visited=None):
    visited = visited if visited else {}
    if node in visited:
        return visited[node]

    new_node = Node()
    visited[node] = new_node


    for neighbor in node.neighbors:
        temp_node = deepcopy(neighbor, visited)
        new_node.neighbors.append(temp_node)

    return new_node


result = deepcopy(nodeA)
