from unittest import TestCase

from string_rotation import string_rotation

class TestStringRotation(TestCase):

    def test_string_rotation(self):

        assert string_rotation("erbottlewat", "waterbottle")

        assert not string_rotation("bottlewat", "waterbottle")

