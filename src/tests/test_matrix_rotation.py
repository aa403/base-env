from unittest import TestCase
from matrix_rotation import matrix_rotation, set_to_zero_small


class TestMatrixRotation(TestCase):

    def test_1(self):
        assert matrix_rotation([[1]]) == [[1]]

        m = [[1]]
        assert matrix_rotation(m) == [[1]]
        # assert matrix_rotation(m) is m

    def test_2(self):
        assert matrix_rotation([
            [1, 0],
            [2, 0]
        ]) == [
                   [2, 1],
                   [0, 0]
               ]

        assert matrix_rotation([
            [1, 2],
            [0, 0]
        ]) == [
                   [0, 1],
                   [0, 2]
               ]

        assert matrix_rotation([
            [1, 2],
            [0, 3]
        ]) == [
                   [0, 1],
                   [3, 2]
               ]

    def test_3(self):
        assert matrix_rotation([
            [1, 0, 0],
            [2, 0, 0],
            [3, 0, 0],
        ]) == [
                   [3, 2, 1],
                   [0, 0, 0],
                   [0, 0, 0],
               ]

        assert matrix_rotation([
            [1, 2, 3],
            [0, 0, 0],
            [0, 0, 0],
        ]) == [
                   [0, 0, 1],
                   [0, 0, 2],
                   [0, 0, 3],
               ]

        assert matrix_rotation([
            [1, 2, 3],
            [4, 0, 5],
            [0, 0, 0],
        ]) == [
                   [0, 4, 1],
                   [0, 0, 2],
                   [0, 5, 3],
               ]


class TestSetToZero(TestCase):

    def test_it(self):
        assert set_to_zero_small([[0]]) == [[0]]

        assert set_to_zero_small([
            [0, 1],
            [2, 0]
        ]) == [
                   [0, 0],
                   [0, 0]
               ]

        assert set_to_zero_small([
            [0, 1],
            [2, 3]
        ]) == [
                   [0, 0],
                   [0, 3]
               ]

        assert set_to_zero_small([
            [3, 0, 1, 4],
            [2, 1, 6, 1],
            [5, 4, 2, 0]
        ]) == [
                   [0, 0, 0, 0],
                   [2, 0, 6, 0],
                   [0, 0, 0, 0]
               ]
