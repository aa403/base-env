"""
Given two strings, write a method to decide if one is a permutation of the
other.
"""

from collections import defaultdict


def sola(a: str, b: str) -> bool:
    a_ctr = defaultdict(int)
    b_ctr = defaultdict(int)

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        a_ctr[a[i]] += 1
        b_ctr[b[i]] += 1

    if a_ctr != b_ctr:
        return False

    return True


def solb(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    ctr = defaultdict(int)

    for i in range(len(a)):
        ctr[a[i]] += 1
        ctr[b[i]] -= 1

        if ctr[a[i]] == 0:
            del ctr[a[i]]

        if ctr[b[i]] == 0:
            del ctr[b[i]]

    if ctr:
        return False

    return True


def check_is_a_permutation(a: str, b: str):
    return solb(a, b)
