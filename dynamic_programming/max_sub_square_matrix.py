"""
Find Maximum Sub Square for a given matrix

1) Create a temp matrix of (row+1) * (col+1)
2) Fill up first row and col with 0
3) Start with [row+1][col+1] cell
4) If matrix[row][col] == 1, then,
    min(
        matrix[row-1][col-1],
        matrix[row][col-1],
        matrix[row-1][col-1]
    ) + 1
5) Keep a max_count variable to store max value derived from point 4
6) Return max_count
"""


def max_sub_square(matrix=None):
    """
    Return max sub square for a given matrix
    """
    if matrix is None:
        return None

    rows = len(matrix) + 1
    cols = len(matrix[0]) + 1

    max_count = 0

    count_matrix = [[0 for col_index  in range(cols)] for row_index in range(rows)]

    for row_index in range(1, rows):
        for col_index in range(1, cols):
            if matrix[row_index - 1][col_index - 1] == 1:
                count_matrix[row_index][col_index] = min(
                    count_matrix[row_index][col_index - 1],
                    count_matrix[row_index - 1][col_index],
                    count_matrix[row_index - 1][col_index - 1]
                ) + 1
                max_count = max(max_count, count_matrix[row_index][col_index])

    return max_count



if __name__ == "__main__":
    print "############"
    print "## Test 1 ##"
    print "############"
    matrix = [
        [0, 1, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1]
    ]
    expected_result = 3
    actual_result = max_sub_square(matrix)
    assert expected_result == actual_result


    print "############"
    print "## Test 2 ##"
    print "############"
    matrix = [
        [0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1]
    ]
    expected_result = 3
    actual_result = max_sub_square(matrix)
    assert expected_result == actual_result

    print "############"
    print "## Test 3 ##"
    print "############"
    matrix = [
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    expected_result = 4
    actual_result = max_sub_square(matrix)
    assert expected_result == actual_result
