"""
Maximum Sum Subarray using Kadane's algorithm

Given an array, find maximum sum sequence subarray
eg:
    input: [-1, -2, 3, 4, -5, 6]

    output = [3, 4, -5, 6] # total = 8

    Here 8 is max sum for a subarray
"""
import sys

class MaxVal(object):
    def __init__(self, value=None, start_index=None, end_index=None):
        self.value = value if value else -1 * sys.maxint
        self.start_index = start_index if start_index else 0
        self.end_index = end_index if end_index else 0

    def get_value(self):
        return self.value

    def __repr__(self):
        return "value: {}, start_index: {}, end_index: {}".format(
            self.value, self.start_index, self.end_index
        )

def max_sum_subarray(array=None):
    if array is None:
        return array

    if len(array) == 1:
        return (array[0], 0, 0) # first number, start_index, end_index

    first_val = array[0]
    max_curr = MaxVal(value=first_val, start_index=0, end_index=0)
    max_global = MaxVal(value=first_val, start_index=0, end_index=0)

    for index in range(1, len(array)):
        val = max_curr.value + array[index]
        if array[index] > val:
            max_curr.value = array[index]
            max_curr.start_index = index
            max_curr.end_index = index
        else:
            max_curr.value = val
            max_curr.end_index = index

        if max_curr.value > max_global.value:
            max_global.value = max_curr.value
            max_global.start_index = max_curr.start_index
            max_global.end_index = max_curr.end_index

    return max_global

if __name__ == '__main__':
    # Happy case
    input_array1 = [-1, -2, 3, 4, -5, 6]
    expected_output = (8, [3, 4, -5, 6]) # total_count, subarray
    result = max_sum_subarray(input_array1)
    # we add +1 to end_index, because Python slicing prints until (end_index - 1) location
    actual_output = (result.value, input_array1[result.start_index: result.end_index + 1])
    assert expected_output == actual_output

    input_array2 = [-4, 15, -6, 18, 2, -20]
    expected_output = (29, [15, -6, 18, 2]) # total_count, subarray
    result = max_sum_subarray(input_array2)
    actual_output = (result.value, input_array2[result.start_index: result.end_index + 1])
    assert expected_output == actual_output
