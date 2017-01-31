"""
Implement Quick Sort recursive

Steps: Follow divide and conquer technique
    1) Select mid as pivot (divides the array in 2 parts, left part < pivot and right part > pivot
    2) i = 0
    3) j = len(array) -1
    4) Increment i until array[i] < array[pivot], if greater, then stop
    5) Decrement j until array[j] > array[pivot], if smaller, then stop
    6) if i <=j then swap table[i] with table[j]
    7) Start from step 4 again, until i<=j
    8) After, i and j cross each other,
      1) if j > start: then recursively call quick_sort(array, start, j)
      2) if i < end: then recursively call quick_sort(array, i, end)

"""


def quick_sort(table, start, end):
    if start == end:
        return table

    i = start
    j = end
    pivot = (start + end) // 2

    while(i <= j):
        while(table[i] < table[pivot]):
            i += 1

        while(table[j] > table[pivot]):
            j -= 1

        if (i <= j):
            table[i], table[j] = table[j], table[i]
            i += 1
            j -= 1


    if j > start:
        quick_sort(table, start, j)
    if i < end:
        quick_sort(table, i, end)


    return table

if __name__ == '__main__':
    table = [5, 1, 4, 2, 10, 99, 0]
    expected_result = sorted(table)
    print table
    print "After sort"
    quick_sort(table, 0, len(table) - 1)
    print table
    assert expected_result == table