"""
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
"""

from collections import defaultdict


def _a(s: str) -> bool:
    res = defaultdict(int)

    for char in s:
        if char.isspace():
            continue

        res[char.lower()] = (res[char.lower()] + 1) % 2

        if res[char.lower()] == 0:
            del res[char.lower()]

    if sum(res.values()) > 1:
        return False

    return True


def _b(s: str) -> bool:
    res = defaultdict(int)

    ctr = 0

    for char in s:
        if char.isspace():
            continue

        char_value = char.lower()

        if res[char_value] % 2 == 0:
            ctr += 1
            res[char_value] = 1
        else:
            ctr -= 1
            res[char_value] = 0

        # if res[char.lower()] == 0:
        #     del res[char.lower()]

    return ctr <= 1


def palindrome_permutation(s: str) -> bool:
    return _b(s)
