#!/usr/bin/python3
"""Define method to generate Pascal's Triangle."""


def pascal_triangle(n):
    """
    Return a pascal triangle of n.
    Return a list of lists of integers representing
    pascal's triangle of n in time O(n^2).
    """
    pascal_triangle = []
    for i in range(1, n + 1):
        row = []
        # first value in a line is always 1
        K = 1
        for j in range(1, i + 1):
            row.append(K)

            # using Binomial Coefficient
            K = K * (i - j) // j

        pascal_triangle.append(row)

    return pascal_triangle
