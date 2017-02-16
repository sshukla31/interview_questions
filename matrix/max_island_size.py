"""
Find Connected Islands OR
Solve 'Connected Cells' Using DFS

Input: n*n matrix
Output: (total no of islands, max_sized_island)

** References:
    Cracking the Coding Interview (https://www.youtube.com/watch?v=R4Nh-EgWjyQ)
"""

def get_island_size(islands, row, col):
    """ Get total size of the island """
    if any([
        row < 0,
        col < 0,
        row >= len(islands),
        col >= len(islands[0]),
    ]):
        return 0
    elif islands[row][col] == 0:
        return 0
    else:
        islands[row][col] = 0
        size = 1
        for sub_row in xrange(row - 1, row + 2):
            for sub_col in xrange(col - 1, col + 2):
                size += get_island_size(islands, sub_row, sub_col)

    return size


def get_islands_info(islands):
    """ Get island info containing total no of islands and max size of the island """
    row_len = len(islands)
    col_len = len(islands[0])

    total_islands = 0
    max_island_size = 0

    for row in xrange(row_len):
        for col in xrange(col_len):
            if islands[row][col] == 1:
                total_islands += 1
                max_island_size = max(
                    max_island_size,
                    get_island_size(islands, row, col)
                )

    return total_islands, max_island_size


if __name__ == '__main__':
    # Test Cases

    print "############## Test 1 ##############"
    islands = [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    total_islands, max_island_size = get_islands_info(islands)
    print "Total number of islands: {} \nMax island size: {}".format(
        total_islands,
        max_island_size
    )
    expected_output = (4, 7)
    actual_output   = (total_islands, max_island_size)

    assert expected_output == actual_output

    print "############## Test 2 ##############"
    islands = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]

    total_islands, max_island_size = get_islands_info(islands)
    print "Total number of islands: {} \nMax island size: {}".format(
        total_islands,
        max_island_size
    )
    expected_output = (5, 4)
    actual_output   = (total_islands, max_island_size)

    assert expected_output == actual_output