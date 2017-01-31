"""
Find a pair of elements from an array whose sum equals a given number

eg:
    input:
        array = [1, 4, -2, 3, 5]
        target = 4

    output = 1, 3


Algo:
    1) Traverse each element and check if number is present in hash_table
    2) If yes, return (array[current_index], array[hash_table[element]])
    3) If absent, then, hash_table[target - array[current_index]] = index

Steps:  hash_table = {}, where, key=target-value and value=current_index
    1) value = 1  | diff = target(4) - value(1) = 3  |  hash_table = {3: 0}
    2) value = 4  | diff = 0 | hash_table = {3:0, 0: 1}
    3) value = -2 | diff = 6 | hash_table = {3:0, 0:1, 6:2}
    4) value = 3, 3 is present in the hash_table, hence, numbers present
"""

def get_pair(array, target):
    diff_index_map = {}
    for index, element in enumerate(array):
        if element in diff_index_map:
            return (True, array[diff_index_map[element]], index)
        else:
            diff = target - element
            diff_index_map[diff] = index

    return (False, None, None)



if __name__ == '__main__':
    array = [1, 4, -2, 3, 5]

    # happy case: elements present
    target = 4
    actual_output = get_pair(array, target)
    expected_output = (True, 1, 3)
    assert expected_output == actual_output

    # failure case: elements not present
    target = 10
    actual_output = get_pair(array, target)
    expected_output = (False, None, None)
    assert expected_output == actual_output

