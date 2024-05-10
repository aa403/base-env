from unittest import TestCase
from palindrome_permutation import palindrome_permutation


class TestPalindromPermutation(TestCase):

    def test_it(self):
        assert palindrome_permutation("b")
        assert palindrome_permutation("B")
        assert palindrome_permutation("bb")
        assert palindrome_permutation("bB")

        assert palindrome_permutation("bob")
        assert palindrome_permutation("boB")  # not case sensitive
        assert palindrome_permutation("b o b")
        assert palindrome_permutation("b  bo")

        assert palindrome_permutation("bodadob")
        assert palindrome_permutation("bod a dob")
        assert palindrome_permutation("bod a d ob")
        assert palindrome_permutation("bo boadd")

        assert not palindrome_permutation("ba")
        assert not palindrome_permutation("bobb")
        assert not palindrome_permutation("bo boaddo")

        assert palindrome_permutation("abcdeabcde")
        assert not palindrome_permutation("abcde")
