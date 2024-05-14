from unittest import TestCase
from string_compression import string_compression


class TestStringCompression(TestCase):

    def test_it(self):
        assert string_compression("a") == "a"
        assert string_compression("ab") == "ab"
        assert string_compression("abc") == "abc"
        assert string_compression("abca") == "abca"
        assert string_compression("aA") == "aA"

        assert string_compression("aa") == "aa"
        assert string_compression("aaa") == "a3"
        assert string_compression("aaaA") == "aaaA"
        assert string_compression("aaaaA") == "a4A1"
        assert string_compression("aabc") == "aabc"
        assert string_compression("abcaa") == "abcaa"
        assert string_compression("aabcccccaaa") == "a2b1c5a3"
