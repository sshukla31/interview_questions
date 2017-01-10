'''
Implementation of ternary expression to Binary Tree

eg:

1)
a?b:c to

  a
 /  \
b   c


2)
a?b?c:d:e to

     a
    / \
   b   e
  / \
 c   d


Algorithm:
1) Create root node and push to stack
2) Create a variable last char to remember ? or :
2) Check of expression ? or :
3) If expression is '?', save last char and then go to the next char
4) When last char is
    ?  - then assign the new node to left of the node on the stack
    :  - then pop the top of the stack as it's a sibling, then pop the stack until
         we find a node whose right child is None. Assign the new node as right child
         of this stack node whose right child is None
5) Push the node


I have used last_char because I was not finding an easy way to for loop with
2 steps and get the index number so as to directly access the element
'''


from commons.stack import Stack

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_tree(node, result):
    if node is not None:
        inorder_tree(node.left, result)
        result.append(node.data)
        inorder_tree(node.right, result)



def ternary_to_binary_tree(expression):
    stack = Stack()
    root = Node(expression[0])
    stack.push(root)
    last_char = None

    for char in expression[1:]:
        if char in ['?', ':']:
            last_char = char
        else:
            node = Node(char)
            if last_char == "?":
                stack.peek().left = node

            if last_char == ':':
                stack.pop()
                while(stack.peek().right != None):
                    stack.pop()
                stack.peek().right = node


            stack.push(node)

    return root

if __name__ == '__main__':
    test = "a?b?c?:d:e"
    root_node = ternary_to_binary_tree(test)
    expected_result = ['c', 'b', 'd', 'e', 'a']
    actual_result = []
    inorder_tree(node=root_node, result=actual_result)
    print expected_result
    print actual_result




