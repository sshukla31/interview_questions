"""
Find Largest Continuous Sub-sequence Zero Sum

Input:  {1, 2, -2, 4, -4}
Output: {2, -2, 4, -4}

"""

def get_largest_cont_subsequence(array):
    array_size = len(array)
    count_array = [0] * (array_size + 1)
    # extra padding. very important
    # we don't have to initialize here but to make it clear we have
    count_array[0] = 0

    # maintain index of integer when last time encountered
    index_map = {}
    last_val = 0

    for index, val in enumerate(array):
        last_val = array[index] + last_val
        count_array[index + 1] = last_val
        index_map[last_val] = index + 1

    for index, val in enumerate(array):
        if val in index_map and index != index_map[val]:
            start_of_seq = index + 1
            end_of_seq = index_map[val]
            return (True, start_of_seq, end_of_seq)

    return (False, None, None)



if __name__ == '__main__':
    array = [1, 2, -2, 4, -4]
    actual_output = get_largest_cont_subsequence(array)
    if actual_output[0]:
        print array[actual_output[1]: actual_output[2]]

    expected_output = (True, 1, 5)

    assert actual_output == expected_output
