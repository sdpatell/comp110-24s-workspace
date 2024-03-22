"""EX04 Utils."""

__author__: str = "730671755"


def all(numbers: list[int], given_number: int) -> bool:
    """Check if numbers match the indicated number."""
    if not numbers:
        return False
    
    idx = 0 

    while idx < len(numbers):
        if numbers[idx] != given_number:
            return False 
        idx += 1
    return True
    

def max(input: list[int]) -> int:
    """The max function is given a list of ints, max will return the largest in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max = input[0]
    idx = 1

    while idx < len(input):
        if input[idx] > max:
            max = input[idx]
        idx += 1
    return max
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    
    idx = 0

    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            return False
    return True
    

def extend(list1: list[int], list2: list[int]) -> None:
    """Using mutate by appending the second lists values."""
    list1.extend(list2)