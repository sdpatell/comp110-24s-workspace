"""Summing the elements of a list using different loops."""

__author__ = "730671755"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements."""
    result = 0.0
    idx = 0

    while idx < len(vals):
        result += vals[idx]
        idx += 1
    return result


def f_sum(vals: list[float]) -> float:
    """Calculating the sum of all elements in vals using for... in...."""
    result = 0.0

    for elem in vals:
        result += elem
    return result


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements using for...in range(...)."""
    result = 0.0

    for idx in range(len(vals)):
        result += vals[idx]
    return result