"""Splitting a dictionary into two lists."""

__author__ = "730671755"

input_dict: dict[str, int] = {}


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """The function will produce a list of all the keys in the input dictionary."""
    keys_list: list[str] = []
    for key in input_dict:
        keys_list += [key]
    return keys_list


def get_values(input: dict[str, int]) -> list[int]:
    """The function will produce a list of all the values in the input dictionary."""
    values_list: list[int] = []
    if input == {}:
        return values_list
    else: 
        for key in input:
            values_list.append(input[key])
    return values_list