"""EX03 Funtional Battleship."""

__author__: str = "730671755"

import random


def input_guess(grid_size: int, specification: str) -> int:
    """Funtion prompts and returns user guess."""
    assert specification == "row" or specification == "column"
    correct = False
    user_guess: int = int(input(f"Guess a {specification}: "))
    while not correct:
        if (user_guess > grid_size) or (user_guess < 1): 
            new_user_guess: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
            if 0 < new_user_guess < grid_size:
                user_guess = new_user_guess
                correct = True
        else:
            correct = True
    return user_guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Prints grid."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    row = 1
    while row <= grid_size:
        grid = ""
        column = 1
        while column <= grid_size: 
            if column_guess == column and row_guess == row:
                if correct_guess: 
                    grid += RED_BOX
                else:
                    grid += WHITE_BOX
            else: 
                grid += BLUE_BOX
            column += 1
        print(grid)
        row += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """The function returns whether or not the user was right given the secret boat location and their guess."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Function that will assemble all of the pieces made for the program."""
    maximum_turns = 5
    current_turn = 1
    win = False
    while not win and current_turn <= maximum_turns: 
        print(f"=== Turn {current_turn}/{maximum_turns} ===")
        user_row = input_guess(grid_size, "row")
        user_column = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_column, user_row, user_column):
            win = True
            print(f"Hit! You won in {current_turn}/{maximum_turns} turns!")
        else:
            print("Miss!")
        print_grid(grid_size, user_row, user_column, True)
        current_turn += 1
    if not win: 
        print(f"Miss! X/{maximum_turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))