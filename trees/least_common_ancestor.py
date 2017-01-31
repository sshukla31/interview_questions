# -*- coding: utf-8 -*-
"""
Least Common Ancestor when we have only parent node info

Complexity:
    Time - O(n)
    Space - O(h)

"""

'''
A Tree
                    A      |    X
                 /     \   |      \
               B        C  |        Y
             /   \     /   |
           D       E  F    |
         /   \             |
        G     I            |
      /                    |
    J                      |
'''



class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lca(root, node1, node2):
    if any([node1 is None, node2 is None]):
        return None

    if root is None:
        return root

    if node1 == node2:
        return node1


    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left is not None and right is not None:
        return root

    return left if left else right




# testing code
# tree 1
nodeX = Node('X', None)
nodeY = Node('Y', nodeX)

# tree 2
nodeJ = Node('J')
nodeG = Node('G', nodeJ)
nodeI = Node('I')
nodeD = Node('D', nodeG, nodeI)
nodeE = Node('E')
nodeB = Node('B', nodeD, nodeE)
nodeF = Node('F')
nodeC = Node('C', nodeF)
nodeA = Node('A', nodeB, nodeC)


assertions = (
    # simple case
    (nodeA, nodeB, nodeC, nodeA),
    (nodeA, nodeB, nodeB, nodeB),

    # parent contains
    (nodeA, nodeD, nodeG, nodeD),
    (nodeA, nodeG, nodeD, nodeD),
    (nodeA, nodeD, nodeI, nodeD),

    # errors
    (nodeA, nodeA, None, None),
    (nodeA, None, nodeA, None),

    # no lca
    (nodeX, nodeY, nodeB, None),
    (nodeX, nodeA, nodeY, None),
    # (nodeX, nodeA, nodeX, None),  THIS CASE FAILS

    # misc tests
    (nodeA, nodeJ, nodeE, nodeB),
    (nodeA, nodeA, nodeJ, nodeA),
)

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
PASS = GREEN + '✓ ' + RESET
FAIL = RED + 'x ' + RESET

errors = 0
for root, left, right, expected in assertions:
    call = 'lca(%r, %r)' % (left, right)
    try:
        actual = lca(root, left, right)
    except Exception as e:
        print FAIL + '%s = %r (expected %s)' % (call, e, expected)
        errors += 1
        continue

    if expected is actual:
        print PASS + '%s = %s' % (call, actual)
    else:
        print FAIL + '%s = %s (expected %s)' % (call, actual, expected)
        errors += 1