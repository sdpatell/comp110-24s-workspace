"""Some functions for my garden plan."""

__author__ = "730671755"


def add_by_kind(by_kind: dict[str, list[str]], plant: str, kind: str) -> None: 
    """Function that adds a plant to a garden dictionary that is sorted by the kind of plant."""
    if kind in by_kind:
        by_kind[kind].append(plant)
    else:
        by_kind[kind] = []
        by_kind[kind].append(plant)


def add_by_date(by_date: dict[str, list[str]], month: str, plant: str) -> None: 
    """Function that adds a plant to a garden dictionary that is sorted by the date in which the seeds should be shown."""
    if month in by_date:
        by_date[month].append(plant)
    else:
        by_date[month] = []
        by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Function that searches through both dictionaries and returns a list of what plants of a certain kind to plant at a certain date."""
    assert kind in plants_by_kind
    assert month in plants_by_date

    kinds_list: list[str] = plants_by_kind[kind]
    dates_list: list[str] = plants_by_date[month]
    combined_list: list[str] = []
    for plant in kinds_list:
        for other_plant in dates_list:
            if plant == other_plant:
                combined_list.append(other_plant)
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}."