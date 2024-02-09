#!/usr/bin/python3
"""
afunction that return a list of lists of integers
"""


def pascal_triangle(n):
    a = []
    if n <= 0:
        return a
    pascal_tri = [[1]]
    while len(pascal_tri) != n:
        tri = pascal_tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascal_tri.append(tmp)
    return pascal_tri
