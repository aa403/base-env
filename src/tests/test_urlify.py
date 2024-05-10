from unittest import TestCase
from urlify import urlify


class TestUrlify(TestCase):

    def test_it(self):
        assert urlify(" ") == "%20"

        assert urlify("Mr John Smith") == "Mr%20John%20Smith"

        assert urlify("Mr John ") == "Mr%20John%20"

        assert urlify(" Mr John ") == "%20Mr%20John%20"

        assert urlify(" Mr John") == "%20Mr%20John"
