#!/usr/bin/python3
"""
Defines function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    parameters:
        n [int]:
            the number of rows of Pascal's triangle to recreate
    return:
        [list of lists of ints]:
            representation of Pascal's triangle
    """

    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n <= 0:
        return triangle
    prev = [1]
    for firstRow in range(n):
        myList = []
        if firstRow == 0:
            myList = [1]
        else:
            for x in range(firstRow + 1):
                if x == 0:
                    myList.append(0 + prev[x])
                elif x == (firstRow):
                    myList.append(prev[x - 1] + 0)
                else:
                    myList.append(prev[x - 1] + prev[x])
        prev = myList
        triangle.append(myList)
    return triangle
