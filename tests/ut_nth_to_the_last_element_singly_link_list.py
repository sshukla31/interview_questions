import unittest
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import nth_to_the_last_element_singly_link_list


class TestNthToLastElement(unittest.TestCase):
    """ Test Cases """
    def setUp(self):
        self.link_list = nth_to_the_last_element_singly_link_list.LinkList()

    def tearDown(self):
        self.link_list = None

    def test_happy(self):
        node_elements = [4, 3, 1, 5, 6, 7, 8]
        for val in node_elements:
            self.link_list.add(val)

        expected_result = [7, 6]
        actual_result = []

        input_elements = [1, 2]
        for element in input_elements:
            actual_result.append(
                self.link_list.find_kth_to_last_element(k=element)
            )

        self.assertEqual(expected_result, actual_result)

    def test_failure(self):
        node_elements = [4, 3, 1, 5, 6, 7, 8]
        for val in node_elements:
            self.link_list.add(val)

        expected_result = [
            "Invalid value k: a",
            "Invalid value k: None",
            "Invalid value k: -1"
        ]
        actual_result = []

        input_elements = ['a', None, -1]
        for element in input_elements:
            actual_result.append(
                self.link_list.find_kth_to_last_element(k=element)
            )

        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()