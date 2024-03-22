"""EX05 - `dict` Unit Tests."""

__author__: str = "730671755"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_1() -> None:
    """Use Case for inverting numbers and letters."""
    numbers_letters: dict[str, str] = {'a': '1', 'b': '2', 'c': '3'}
    expected_output = {'1': 'a', '2': 'b', '3': 'c'}
    assert invert(numbers_letters) == expected_output


def test_invert_2() -> None:
    """Use Case for inverting things."""
    things: dict[str, str] = {'car': 'race', 'book': 'bag', 'hand': 'book'}
    expected_output = {'race': 'car', 'bag': 'book', 'book': 'hand'}
    assert invert(things) == expected_output


def test_invert_3() -> None:
    """Edge Case for inverting the same subjects."""
    subjects: dict[str, str] = {'math': 'math', 'english': 'english', 'history': 'history'}
    expected_output = {'math': 'math', 'english': 'english', 'history': 'history'}
    assert invert(subjects) == expected_output


def test_favorite_color_1() -> None:
    """Use Case for testing the favorite color - red."""
    input: dict[str, int] = {'max': 'red', 'sally': 'pink', 'sarah': 'red', 'ryan': 'blue'}
    popular_color: str = "red"
    assert favorite_color(input) == popular_color


def test_favorite_color_2() -> None:
    """Use Case for testing the favorite color- blue."""
    input: dict[str, int] = {'max': 'blue', 'sally': 'blue', 'sarah': 'red', 'ryan': 'purple'}
    popular_color: str = "blue"
    assert favorite_color(input) == popular_color


def test_favorite_color_3() -> None:
    """Edge Case for testing if everyone has the same favorite color."""
    input: dict[str, int] = {'max': 'blue', 'sally': 'blue', 'sarah': 'blue'}
    popular_color: str = "blue"
    assert favorite_color(input) == popular_color


def test_count_1() -> None:
    """Use Case for counting vegetables."""
    counter: dict[str, int] = ['carrot', 'broccoli', 'carrot', 'mushroom', 'broccoli', 'carrot']
    count_value: dict[str, int] = {'carrot': 3, 'broccoli': 2, 'mushroom': 1}
    assert count(counter) == count_value


def test_count_2() -> None:
    """Use Case for counting flowers."""
    counter: dict[str, int] = ['tulip', 'rose', 'dandelion', 'lily', 'rose', 'dandelion']
    count_value: dict[str, int] = {'tulip': 1, 'rose': 2, 'dandelion': 2, 'lily': 1}
    assert count(counter) == count_value


def test_count_3() -> None:
    """Edge Case for counting duplicates of flowers."""
    counter: dict[str, int] = ['tulip', 'tulip', 'tulip', 'lily', 'lily', 'lily']
    count_value: dict[str, int] = {'tulip': 3, 'lily': 3}
    assert count(counter) == count_value


def test_alphabetizer_1() -> None:
    """Use Case for alphabetizing names."""
    names: list[str] = ['sarah', 'sally', 'max', 'maya']
    result: dict[str, list[str]] = {'s': ['sarah', 'sally'], 'm': ['max', 'maya']}
    assert alphabetizer(names) == result


def test_alphabetizer_2() -> None:
    """Use Case for alphabetizing subjects."""
    subjects: list[str] = ['social studies', 'science', 'math', 'english']
    result: dict[str, list[str]] = {'m': ['math'], 'e': ['english'], 's': ['social studies', 'science']}
    assert alphabetizer(subjects) == result


def test_alphabetizer_3() -> None:
    """Edge Case adding special characters and checking if it will still alphabetize."""
    names: list[str] = ['sarah!', 'sally$', 'max!', 'maya*']
    result: dict[str, list[str]] = {'m': ['max!', 'maya*'], 's': ['sarah!', 'sally$']}
    assert alphabetizer(names) == result


def test_update_attendance_1() -> None:
    """Use Case adding a name to the Monday attendance list."""
    attendance: dict[str, list[str]] = {'Monday': ['Sally', 'Sarah'], 'Tuesday': ['Max']}
    day: str = 'Monday'
    student: str = 'Maya'
    update_attendance(attendance, day, student)
    expected_attendance = {'Monday': ['Sally', 'Sarah', 'Maya'], 'Tuesday': ['Max']}
    assert attendance == expected_attendance


def test_update_attendance_2() -> None:
    """Use Case added a name to the Tuesday attendance list."""
    attendance: dict[str, list[str]] = {'Monday': ['Sally'], 'Tuesday': ['Max', "Sally"]}
    day: str = 'Tuesday'
    student: str = 'Maya'
    update_attendance(attendance, day, student)
    expected_attendance = {'Monday': ['Sally'], 'Tuesday': ['Max', 'Sally', 'Maya']}
    assert attendance == expected_attendance


def test_update_attendance_3() -> None:
    """Edge case adding another day to the attendance."""
    attendance: dict[str, list[str]] = {'Monday': ['Sally'], 'Tuesday': ['Max', "Sally"]}
    day: str = 'Wednesday'
    student: str = 'Maya'
    update_attendance(attendance, day, student)
    expected_attendance = {'Monday': ['Sally'], 'Tuesday': ['Max', 'Sally'], 'Wednesday': ['Maya']}
    assert attendance == expected_attendance