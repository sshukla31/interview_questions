import unittest
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import ternary_to_bt


class TestListElements(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_expression1(self):
        """Test the expression using in-order traversal """
        expression = "a?b?c?:d:e"
        root_node = ternary_to_bt.ternary_to_binary_tree(expression)
        expected_result = ['c', 'b', 'd', 'a', 'e']
        actual_result = []
        ternary_to_bt.inorder_tree(node=root_node, result=actual_result)
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()