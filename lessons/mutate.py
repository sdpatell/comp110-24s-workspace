"""Mutating functions."""

__author__ = "730671755"


def manual_append(letter: list[int], number: int) -> None:
    """Function to mutate its input appending the int parameter to the end of the parameter."""
    letter.append(number)


def double(letter: list[int]) -> None:
    """Function to mutate its input by multiplying every element in the parameter."""
    index = 0
    while index < len(letter):
        letter[index] *= 2
        index += 1