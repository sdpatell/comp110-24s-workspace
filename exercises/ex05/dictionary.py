"""EX05 - Dictionary Functions."""

__author__: str = "730671755"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values."""
    inverted_input: dict[str, str] = {}
    for key in input:
        if input[key] in inverted_input:
            raise KeyError("error message of your choice here!")
        inverted_input[input[key]] = key
    return inverted_input


def favorite_color(input_color: dict[str, str]) -> str:
    """Function returns the favorite color."""
    count_color: dict[str, int] = {}
    popular_color: str = "" 
    maximum = 0

    for key in input_color:
        idx = input_color[key]

        if idx in count_color:
            count_color[idx] += 1
        else:
            count_color[idx] = 1
    
        if count_color[idx] > maximum:
            maximum = count_color[idx]
            popular_color = idx
    return popular_color


def count(counter: list[str]) -> dict[str, int]:
    """Function that has a dictionary of the counts of each of the items in the input list."""
    count_value: dict[str, int] = {}
    for value in counter: 
        if value in count_value:
            count_value[value] += 1
        else:
            count_value[value] = 1
    return count_value


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Function that has a dictionary of the letters and the lists of words that belong to that letter."""
    result: dict[str, list[str]] = {}
    for item in words:
        letter1 = item[0].lower()
        if letter1 in result:
            result[letter1].append(item)
        else:
            result[letter1] = [item]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Function will mutate and return that dictionary."""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]