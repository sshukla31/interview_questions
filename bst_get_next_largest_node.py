# -*- coding: utf-8 -*-

"""
BST (Binary Search Tree) Review:
A Binary Search Tree is a binary tree (2 children: ‘left’ and ‘right’) where every node in the tree follows this
rule:

Given a node, every node in its left subtree must have value smaller than itself and every node in its right subtree
must have value larger than itself.

        5
    3       8
  1   4   6   9
0   3.5

e.g.:
input:
5
4
1
8
output:
6
5
3
9

Problem: You have a BST where each node has pointers to its two children AND to its parent.
Given a node in the BST, find the next largest node in the BST, e.g. if all the nodes were sorted by value in
ascending order, it would be the next on the sorted list.

struct Node {
    Node *left;
    Node *right;
    Node *parent;
}
Node *nextLargestNode(Node *n);


ROOT IS NOT PROVIDED



Steps:
  HAS RIGHT NODE:
    1) If node has a right node, go to right node's left most node and return. If no child is present for right node
       return right_node
  HAS NO RIGHT NODE:
    1) If node has no right node and it's node.parent.left == node, return parent
    2) else: go to parent

"""

class Node(object):
    def __init__(self, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent


def get_next_largest(node):
    if node is None:
        return None

    if all([
        node.parent is None,
        node.left is None,
        node.right is None
    ]):
        return None

    if node.right:
        node = node.right
        while(node.left != None):
            node = node.left

        return node
    else:
        while(node.parent != None):
            parent = node.parent
            if parent.left == node:
                return parent
            else:
                node = parent


    return None



node0 = Node()
node1 = Node()
node2 = Node()
node3 = Node()
node3_5 = Node() # i.e 3.5
node4 = Node()
node5 = Node()
node6 = Node()
node8 = Node()
node9 = Node()

# root
node5.left = node3
node5.right = node8

# left sub-tree
node3.left = node1
node3.right = node4
node3.parent = node5
node1.left = node0
node1.parent = node3
node0.parent = node1
node4.left = node3_5
node4.parent = node3
node3_5.parent = node4

# right sub-tree
node8.left = node6
node8.right = node9
node8.parent = node5
node6.parent = node8
node9.parent = node8

# fake node
node11 = Node()

assertions = (
    # simple case
    (node0, node1),
    (node4, node5),
    (node5, node6),
    (node9, None),
    (node1, node3),
    (node8, node9),
    (node11, None)
)

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
PASS = GREEN + '✓ ' + RESET
FAIL = RED + 'x ' + RESET

errors = 0
for node_input, expected in assertions:
    call = 'get_next_largest(%r)' % (node_input)
    try:
        actual = get_next_largest(node_input)
    except Exception as e:
        print FAIL + '%s = %r (expected %s)' % (call, e, expected)
        errors += 1
        continue

    if expected is actual:
        print PASS + '%s = %s' % (call, actual)
    else:
        print FAIL + '%s = %s (expected %s)' % (call, actual, expected)
        errors += 1