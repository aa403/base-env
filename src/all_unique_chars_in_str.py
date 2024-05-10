"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

"""
from collections import defaultdict


def all_unique(s: str):
    d = defaultdict(int)

    for char in s:
        d[char] += 1
        if d[char] != 1:
            return False

    return True


def all_unique__str_only(s: str):
    d = defaultdict(int)

    for char in s:
        d[char] += 1
        if d[char] != 1:
            return False

    return True
