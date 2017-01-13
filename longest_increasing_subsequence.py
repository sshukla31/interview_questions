"""
Longest Increasing Subsequence

Soution:
    1) We can solve this using Dynamic Programming
    2) Create a temporary array of len(sequence)
    3) Update the temporary array count for the corresponding sequence element
    4) Get the max count in the array. This is our result

    # sequence  - array input
    # seq_count - temporary array to keep max subsequence count
    if sequence[i] < sequence[j]:
        seq_count[j] = max(seq_count[j], seq_count[i] + 1)


Steps:
    1) Create a temporary array of sizeof subsequence and initialize with value 1
    2) Create 2 index pointers i and j, where i=0 and j=1
    3) Iterate through input sequence using j pointer
    4) Following rules needs to be applied while moving the pointer,
       A) If i == j,
            Set i=0 and j=j+1
       B) If value at subsequence[i] < subsequence[j],
            1) update temporary_array[j] = max(temporary_array[j], temporary_array[i] + 1)
            2) Set i=i+1
            3) update max_count variable - Holds max subsequence count and avoids iterating array over again
               to get max val
    4) Return max_count

Complexity:
    Time:  O(n^2)
    Space: O(n)

Reference:
    * http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
"""



def longest_increasing_subsequence(sequence):

    if len(sequence) == 0:
        return 0

    seq_count = [1] * len(sequence)  # temporary array
    max_count = 1                    # max subsequence count

    for j in xrange(1, len(sequence)):
        i = 0
        while(i < j):
            if sequence[i] < sequence[j]:
                tmp_count = max(seq_count[j], seq_count[i] + 1)
                seq_count[j] = tmp_count
                max_count = max(max_count, tmp_count)

            i += 1

    return max_count

if __name__ == '__main__':
    sequence1 = [23, 10, 22, 5, 33, 8, 9, 21, 50, 41, 60, 80, 99, 22, 23, 24, 25, 26, 27]
    sequence2 = [3, 4, -1, 0, 6, 2, 3]
    sequence3 = [2, 5, 1, 8, 3]
    expected_result = [10, 4, 3]
    actual_result = [
        longest_increasing_subsequence(sequence)
        for sequence in [sequence1, sequence2, sequence3]
    ]
    assert expected_result == actual_result