"""
Longest Common Substring

Solution: DP
    1) Create a matrix, (n+1) * (m+1)
    2) Loop second word say pointer i and a nested loop for first word say pointer j
    3) If characters are same, eg: 'a' == 'a'
        count_matrix[i][j] = count_matrix[i-1][j-1] + 1
    4) Keep max_len variable to keep track of maximum value
    5) Return value


Complexity:
    Time: O(2^m) assuming m is bigger than n
    Space: O(n*m)

"""

def longest_common_substring(first, second):
    # Create one extra row and col filled with 0 for DP. As this records distance
    # to char itself and also required to access count_matrix[row - 1][col - 1]
    rows = len(second) + 1
    cols = len(first) + 1
    # count_matrix1 = [[0]*cols] * rows   # This doesn't work.Avoid for multi-dimensional array
    count_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    max_len = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if second[i - 1] == first[j - 1]:
                val = count_matrix[i-1][j-1] + 1
                count_matrix[i][j] = val
                max_len = max(max_len, val)

    return max_len


if __name__ == '__main__':
    first = "abcdef"
    second = "zcdemf"
    expected_result = 3
    actual_result = longest_common_substring(first, second)
    assert expected_result == actual_result

    first = "sentimental"
    second = "judgemental"
    expected_result = 6
    actual_result = longest_common_substring(first, second)
    assert expected_result == actual_result
