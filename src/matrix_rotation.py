"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""
from typing import List


def _b(matrix: List[List[int]]) -> List[List[int]]:
    """perform a 90 degree clockwise rotation: which is either
    - M[i, j] -> M[j, (n-i-1)%n]
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]

    return matrix


def _a(matrix: List[List[int]]) -> List[List[int]]:
    """perform a 90 degree clockwise rotation: which is either
    - a transpose followed by mirroring the rows
    - col(i) -> row(i), row(i) -> col(i-1)
    """

    n: int = len(matrix)

    new_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for col in range(n):
            new_matrix[col][(n - row - 1) % n] = matrix[row][col]

    return new_matrix


def matrix_rotation(*args) -> List[List[int]]:
    return _a(*args)


def set_to_zero(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    rows_to_zero = []
    cols_to_zero = []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                rows_to_zero.append(r)
                cols_to_zero.append(c)

    for c in cols_to_zero:
        for r in range(rows):
            matrix[r][c] = 0

    for r in rows_to_zero:
        for c in range(cols):
            matrix[r][c] = 0

    return matrix


def set_to_zero_small(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])

    row0_to_zero = False
    col0_to_zero = False

    for c in range(cols):
        if matrix[0][c] == 0:
            row0_to_zero = True

    for r in range(rows):
        if matrix[r][0] == 0:
            col0_to_zero = True

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for c in range(1, cols):
        if matrix[0][c] == 0:
            for r in range(1, rows):
                matrix[r][c] = 0

    for r in range(1, rows):
        if matrix[r][0] == 0:
            for c in range(1, cols):
                matrix[r][c] = 0

    if row0_to_zero:
        matrix[0] = [0] * cols

    if col0_to_zero:
        for r in range(1, rows):
            matrix[r][0] = 0

    return matrix
