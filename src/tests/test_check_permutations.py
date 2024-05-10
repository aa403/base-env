from unittest import TestCase
from check_permutation import check_is_a_permutation


class TestIsUnique(TestCase):

    def test_check_is_a_permutation(self):
        assert check_is_a_permutation("a", "a")
        assert check_is_a_permutation("ab", "ba")
        assert check_is_a_permutation("abc", "bac")

    def test_not_check_is_a_permutation(self):
        assert not check_is_a_permutation("a", "b")
        assert not check_is_a_permutation("ab", "bc")
        assert not check_is_a_permutation("ab", "abc")
