from unittest import TestCase
from all_unique_chars_in_str import all_unique


class TestIsUnique(TestCase):

    def test_is_unique(self):
        assert all_unique("a")
        assert all_unique("ab")
        assert all_unique("abc")
        assert all_unique("abcABC")
        assert all_unique("abcdefghijklmnopA")

        assert not all_unique("aa")
        assert not all_unique("abcda")
        assert not all_unique("abcdb")
