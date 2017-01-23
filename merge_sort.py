"""
Implement Merge Sort

*Reference: Algorithms in Python (Michael T. Goodrich)
"""


def merge(left, right, sorted_array):
    i = j = 0  # i points to first index of left and j to right

    # traverse, compare left array & right array value & copy into sorted_array
    # There are total 4 cases:
    # A) Cases when we copy from left[i] to sorted_array[i+j]
    #   1. [left[i] < right[j] and i < len(left)], then, copy from left[i] to sorted_array[i+j]
    #   2. pointer j has reached end. (j == len(right)), then, copy remaining element of left array to sorted_array
    # B) Cases when we copy from right[j] to sorted_array[i+j]
    #   3. left[i] < right[j], then, copy from right[j] to sorted_array [i+j]
    #   4. pointer i has reached end. (i == len(left)), then, copy remaining element of right array to sorted_array


    # Case1 & Case 2 are implemented in 'if' conditon and Case 3 & 4 handles 'else' condition
    while i + j < len(sorted_array):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            sorted_array[i+j] = left[i]
            i += 1
        else:
            sorted_array[i+j] = right[j]
            j += 1


def merge_sort(unsorted_array):
    array_size = len(unsorted_array)
    if array_size < 2:
        return

    # Divide
    mid = array_size / 2
    left = unsorted_array[0: mid]
    right = unsorted_array[mid: ]

    # Conquer
    merge_sort(left)
    merge_sort(right)

    # Merge
    merge(left, right, unsorted_array)



if __name__ == '__main__':
    unsorted_array = [
        85, 24, 63, 45, 17, 31, 96, 50
    ]

    merge_sort(unsorted_array)
    expected_result = sorted(unsorted_array)
    assert expected_result == unsorted_array
