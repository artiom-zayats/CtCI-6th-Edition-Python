# O(MxN)
import unittest
from copy import copy, deepcopy


def mysol(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    ans = deepcopy(matrix)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                #zero col
                for i in range(rows):
                    ans[i][col] = 0
                for i in range(cols):
                    ans[row][i] = 0
    return ans


def mysol2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                #zero col
                for i in range(rows):
                    if matrix[i][col] != 0:
                        matrix[i][col] = None
                for i in range(cols):
                    if matrix[row][i] != 0:
                        matrix[row][i] = None

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == None:
                matrix[row][col] = 0
    return matrix


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []
    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            matrix[idx] = [0] * len(matrix[0])
    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix


class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [mysol,mysol2,zero_matrix, zero_matrix_pythonic]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
