#!/usr/bin/python3
"""
Given a number n, write a method that calculates the
fewest number of operations needed to result in exactly
n H characters in the file.
"""


def minOperations(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    end_str = "H"
    copy_str = ""

    str_len = 1
    oper_total = 0

    while str_len < n:
        if n % str_len == 0:
            copy_str = end_str  # copy
            oper_total += 1
        end_str += copy_str     # paste
        str_len = len(end_str)
        oper_total += 1
    return oper_total
