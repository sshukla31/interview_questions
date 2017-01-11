"""
Check if 2 strings are anagram
"""

from collections import defaultdict


def is_anagram(first, second):
    char_count = defaultdict(int)

    for char in first:
        char_count[char] += 1

    for char in second:
        count = char_count.get(char)
        if not count:
            return False

        if count == 1:
            char_count.pop(char)
        else:
            char_count[char] -= 1

    return True if len(char_count) == 0 else False


if __name__ == '__main__':
    # Case 1
    first = "listen"
    second = "silent"
    result = is_anagram(first, second)
    assert result == True

    # Case 2
    first = "listen"
    second = "silent1"
    result = is_anagram(first, second)
    assert result == False

    # Case 3
    first = "listen1"
    second = "silent"
    result = is_anagram(first, second)
    assert result == False