# -*- coding: utf-8 -*-

'''
A Tree
                    A      |    X
                 /     \   |      \
               B        C  |        Y
             /   \     /   |
           D       E  F    |
         / | \             |
        G  H  I            |
      /                    |
    J                      |
'''



class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def __repr__(self):
        return '<Node:%s>' % self.value


def lca(left, right):
    '''Find the lowest common ancestor of two nodes
    Given two Node objects, return the first common parent, or None
    if the nodes have no parents in common.
    Examples using tree above:
        Given nodes B and C, return node A
        Given nodes J and E, return node B
    '''

    if any([left is None, right is None]):
        return None

    from sets import Set
    visited = Set([])

    if left == right:
        return left

    while(left != None):
        visited.add(left)
        left = left.parent


    while(right != None):
        if right in visited:
            return right
        else:
            right = right.parent


    return None



# testing code
# tree 1
nodeX = Node('X', None)
nodeY = Node('Y', nodeX)

# tree 2
nodeA = Node('A', None)

nodeB = Node('B', nodeA)
nodeC = Node('C', nodeA)

nodeD = Node('D', nodeB)
nodeE = Node('E', nodeB)
nodeF = Node('F', nodeC)

nodeG = Node('G', nodeD)
nodeH = Node('H', nodeD)
nodeI = Node('I', nodeD)

nodeJ = Node('J', nodeG)


assertions = (
    # simple case
    (nodeB, nodeC, nodeA),
    (nodeB, nodeB, nodeB),

    # parent contains
    (nodeD, nodeG, nodeD),
    (nodeG, nodeD, nodeD),
    (nodeD, nodeI, nodeD),

    # errors
    (nodeA, None, None),
    (None, nodeA, None),

    # no lca
    (nodeY, nodeB, None),
    (nodeA, nodeX, None),

    # misc tests
    (nodeJ, nodeE, nodeB),
    (nodeA, nodeJ, nodeA),
)

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
PASS = GREEN + '✓ ' + RESET
FAIL = RED + 'x ' + RESET

errors = 0
for left, right, expected in assertions:
    call = 'lca(%r, %r)' % (left, right)
    try:
        actual = lca(left, right)
    except Exception as e:
        print FAIL + '%s = %r (expected %s)' % (call, e, expected)
        errors += 1
        continue

    if expected is actual:
        print PASS + '%s = %s' % (call, actual)
    else:
        print FAIL + '%s = %s (expected %s)' % (call, actual, expected)
        errors += 1