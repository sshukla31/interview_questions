"""
Write a program to print all permutations of a given string

eg: ABC  -> ABC, ACB, BAC, BCA, CBA, CAB

**References:
    http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

"""

def permute(str_input, start_index, end_index, result):
    result = [] if result is None else result

    if start_index == end_index:
        result.append(str(str_input))
    else:
        for curr_index in xrange(start_index, end_index + 1):
            # swap
            str_input[start_index], str_input[curr_index] = str_input[curr_index], str_input[start_index]
            permute(str_input, start_index + 1, end_index, result)
            # swap back again to maintain original string - backtrack
            str_input[start_index], str_input[curr_index] = str_input[curr_index], str_input[start_index]


def main():
    str_input_1 = bytearray("ABC")
    expected_output = ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']
    actual_output = []
    permute(str_input_1, 0, len(str_input_1) - 1, actual_output)
    assert expected_output == actual_output


if __name__ == '__main__':
    main()