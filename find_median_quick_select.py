'''
Find median:

1) odd elements: [0, 1, 2]
   median = 1
2) even elements: [0, 1, 2, 3]
   median = (1 + 2)/2 = 1.5

Steps:
    Divide and Conquer using quick select: Find kth max in the list. kth max will
    be list_lenght/2 for odd and (list_length/2 + list_length/2 - 1) / 2.

    This algorithm can also be used to find kth max element instead of median too.
    However, we then need to pass k value manually.


    1) Select random pivot
    2) create 3 lists,
       a) lows = all no less than pivot
       b) highs = all no higher than pivot
       c) pivots = all equal to pivot
    3) Then check if the k(kth max count) is less than lows count. If yes, then
       we only look in lows count
    4) If kth max count is equal to lows+pivots count then return pivots[0] as
       we got the answer
    5) If kth max count is greater than lows+points, it means look for highs
    6) We keep doing steps 1 to 5 in recursion and return the result

Complexity: O(n)

'''


import random

def find_median(l):
    l_len = len(l)
    if l_len % 2 == 1:
        result =  quick_select(
            l,
            l_len/2,
            random.choice
        )
    else:
        result =  0.5 * (
            quick_select(l, l_len/2, random.choice) + quick_select(l, (l_len/2) - 1, random.choice)
        )

    return result


def quick_select(l, k, pivot_func):

    if len(l) == 1:
        # optimization
        assert k == 0
        return l[0]

    pivot = pivot_func(l)
    lows = []
    highs = []
    pivots = []


    for num in l:
        if num < pivot:
            lows.append(num)
        elif num > pivot:
            highs.append(num)
        else:
            pivots.append(num)

    if k < len(lows):
        return quick_select(lows, k, pivot_func)
    elif k < (len(lows) + len(pivots)):
        return pivots[0]
    else:
        return quick_select(highs, k - (len(lows) + len(pivots)), pivot_func)




if __name__ == '__main__':
    l = [9,1,0,2,3,4,6,8,7,10,5]
    actual_result = find_median(l)
    expected_result = 5
    assert actual_result == expected_result

    l = [3,2,1,5,6,4]
    actual_result = find_median(l)
    expected_result = 3.5
    assert actual_result == expected_result
