"""
Longest Common Subsequence

eg: str1 = "abcdaf"
    str2 = "acbcf"

    Here, there are 2 largest common subsequence,
     1) abcf - len - 4
     2) abcf - len - 4

     Return longest substring - abcf - 4

Solution: DP
    1) Create a matrix, (n+1) * (m+1)
    2) Loop second word say pointer i and a nested loop for first word say pointer j
    3) If characters are same, eg: 'a' == 'a'
        count_matrix[i][j] = count_matrix[i-1][j-1] + 1
      else:
        count_matrix[i][j] = max(count_matrix[i-1][j], count_matrix[i][j-1])
    4) Keep max_len variable to keep track of maximum value
    5) Return value


Complexity:
    Time: O(2^m) assuming m is bigger than n
    Space: O(n*m)


* Note: Similar to longest common substring with one variant when string don't match
"""

def longest_common_subsequence(first, second):
    """ Find max len longest_common_subsequence for given 2 words """
    # Create one extra row and col filled with 0 for DP. As this records distance
    # to char itself and also required to access count_matrix[row - 1][col - 1]
    rows = len(second) + 1
    cols = len(first) + 1
    # count_matrix1 = [[0]*cols] * rows   # This doesn't work.Avoid for multi-dimensional array
    count_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    max_len = 0
    max_position = (0, 0)  # keep track of the co-ordinate of max_len. This helps to print the longest substring

    for i in range(1, rows):
        for j in range(1, cols):
            if second[i - 1] == first[j - 1]:
                val = count_matrix[i-1][j-1] + 1
            else:
                val = max(count_matrix[i-1][j], count_matrix[i][j-1])

            count_matrix[i][j] = val
            if val > max_len:
                max_len = val
                max_position = (i, j)

    return max_len


if __name__ == '__main__':
    first = "abcdaf"
    second = "acbcf"
    expected_result = 4
    actual_result = longest_common_subsequence(first, second)
    # common subsequence = abcf
    assert expected_result == actual_result

    first = "mentxayl"
    second = "mentpaql"
    expected_result = 6
    actual_result = longest_common_subsequence(first, second)
    # common subsequence = mental
    assert expected_result == actual_result
