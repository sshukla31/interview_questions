"""
Print Binary Tree in level order
"""


class Node(object):
    """ Define node object """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(value=%s)' % (self.value)

def print_level_order(root_node):
    """
    Print tree in level order
    """
    current_level = [root_node]

    while current_level:
        next_level = list()
        for node in current_level:
            print node.value,
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        print

        current_level = next_level


def main():
    tree = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))
    print_level_order(tree)

if __name__ == '__main__':
    main()