"""
Implement KMP substring match algorithm.
The algorithm returns first matching substring
indexes(start, end). This indexes can be used to print
substring from the string.

#TODO: implement search other than match. Search should return
       all matches across the string
"""

def build_prefix_array(pattern):
    pattern_len = len(pattern) if pattern else 0
    if pattern_len == 0:
        return -1
    elif len(pattern) == 1:
        return [0]
    else:
        j = 0
        i = 1
        prefix_array = [0] * pattern_len

        while(i <= pattern_len - 1):
            if pattern[j] == pattern[i]:
                prefix_array[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    prefix_array[i] = 0
                    i += 1
                else:
                    j = prefix_array[j - 1]


    return prefix_array


def compare(string, pattern, prefix_array):
    len_string = len(string) - 1
    len_pattern = len(pattern) - 1

    result = []
    i = j = 0  # i pointer to string and j to pattern
    start_index = end_index = -1

    while(i <= len_string and j <= len_pattern):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = prefix_array[j - 1]
            else:
                i += 1

    if j == len_pattern + 1: # after last match j was incremented, hence + 1
        start_index = i - j
        end_index = i
        result.append((start_index, end_index))

    return result


def kmp(needle, haystack):
    """
    KMP algorithm to return first matching substring
    indexes(start, end)
    """
    prefix_array = build_prefix_array(needle)
    return compare(
        string=haystack,
        pattern=needle,
        prefix_array=prefix_array
    )


if __name__ == '__main__':
    # Test 1: substring present 1 time within the string
    pattern = "abcaby"
    string = "abxabcabcaby"
    expected_prefix_pattern = [0, 0, 0, 1, 2, 0]
    result = kmp(haystack=string, needle=pattern)
    assert pattern == string[result[0][0]: result[0][1]]

    # Test 2: substring present 2 times within the string
    pattern = "abcaby"
    string = "abxabcabcabymdabcaby"
    expected_prefix_pattern = [0, 0, 0, 1, 2, 0]
    result = kmp(haystack=string, needle=pattern)
    assert pattern == string[result[0][0]: result[0][1]]

    # Test 3: substring present 1 time within the string
    pattern = "abcdabca"
    string = "abcdxabcyabcdabcaum"
    expected_prefix_pattern = [0, 0, 0, 0, 1, 2, 3, 1]
    result = kmp(haystack=string, needle=pattern)
    assert pattern == string[result[0][0]: result[0][1]]

    # Test 4: No match found
    pattern = "aabaabaaa"
    string = "abcdxabcyabcdabcaum"
    expected_prefix_pattern = [0, 1, 0, 1, 2, 3, 4, 5, 2]
    result = kmp(haystack=string, needle=pattern)
    assert [] == result
