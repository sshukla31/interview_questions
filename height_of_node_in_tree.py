from commons.binary_tree import BinaryTree


class TreeHeight(object):
    def __init__(self):
        self.root = None

    def max_number(self, root):
        if root is None:
            return root
        elif root.right is None:
            return root
        else:
            self.max_number(root.right)

    def min_number(self, root):
        if root is None:
            return root
        elif root.left is None:
            return root
        else:
            self.max_number(root.left)

    def height_of_tree(self, root):
        if root is None :
            return -1

        return max(
            self.height_of_tree(root.left),
            self.height_of_tree(root.right)
        ) + 1


    def height_of_node(self, root, search_node, height=None):
        height = height if height else 0
        if root is None:
            # node not found
            return None
        if root.data == search_node:
            return height
        elif root.data < search_node:
            height += 1
            return self.height_of_node(root.right, search_node, height)
        else:
            height += 1
            return self.height_of_node(root.left, search_node, height)


if __name__ == '__main__':
    binary_tree = BinaryTree()
    th = TreeHeight()
    elements = [6, 4, 3, 5, 8, 7, 9, 10]

    for element in elements:
        binary_tree.insert(element)

    # Print max height of the tree
    assert th.height_of_tree(binary_tree.root) == 3

    # print height of specific node
    assert th.height_of_node(binary_tree.root, 3), 2

    # print height of specific node
    assert th.height_of_node(binary_tree.root, 10), 3

    # print height of specific node: Node not present
    result = th.height_of_node(binary_tree.root, 11)
    if result is None:
        assert 1 == 1