"""Test my garden functions."""

__author__ = "730671755"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_fruit() -> None: 
    """Use case for testing kinds of fruit."""
    fruit: dict[str, list[str]] = {"Fruit": ["Blueberry"]}
    name_fruit: str = "Banana"
    kind: str = "Fruit"
    assert add_by_kind(fruit, name_fruit, kind) is None


def test_add_by_vegetable() -> None: 
    """Edge case for testing kinds of vegetable."""
    vegetable: dict[str, list[str]] = {"Vegetable": ["Squash"]}
    name_vegetable: str = "Carrot"
    kind: str = "Vegetable"
    assert add_by_kind(vegetable, name_vegetable, kind) is None


def test_add_by_day_december() -> None: 
    """Edge case for testing the fruit in december."""
    month: dict[str, list[str]] = {"December": ["Squash"]}
    name: str = "December"
    fruit: str = "Banana"
    assert add_by_date(month, name, fruit) is None


def test_add_by_date_spinach() -> None: 
    """Use case for testing the date for spinach."""
    month: dict[str, list[str]] = {"May": ["Carrots", "Broccoli"]}
    name: str = "May"
    vegetable: str = "Spinach"
    assert add_by_date(month, name, vegetable) is None


def test_lookup_by_fruits_in_november() -> None:
    """Edge case for testing the fruits in november."""
    name_by_kind: dict[str, list[str]] = {"Fruit": ["Blueberry"], "Vegetable": ["Squash"]}
    name_by_date: dict[str, list[str]] = {"May": ["Carrots", "Broccoli"], "November": ["Squash"]}
    kind: str = "Fruit"
    month: str = "November"
    assert lookup_by_kind_and_date(name_by_kind, name_by_date, kind, month) == "No Fruits to plant in November."


def test_lookup_by_vegetable_in_may() -> None:
    """Use case for testing the vegetables in may."""
    plants_by_kind: dict[str, list[str]] = {"Fruit": ["Blueberry"], "Vegetable": ["Carrots", "Broccoli", "Squash"]}
    plants_by_date: dict[str, list[str]] = {"May": ["Carrots"], "August": ["Broccoli"]}
    kind: str = "Vegetable"
    month: str = "May"
    assert lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month) == "Vegetables to plant in May: ['Carrots']"