"""EX02 One Shot Battleship."""

__author__ = "730671755"

grid_size: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

correct: bool = False

row_number: int = int(input("Guess a row: "))


# check if row guess is to high or low for the grid size
while not correct:
    if (row_number > grid_size) or (row_number < 1): 
        new_row_number: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
        if 0 < new_row_number < grid_size:
            row_number = new_row_number
            correct = True
    else:
        correct = True

correct = False

column_number: int = int(input("Guess a column: "))


# check if column guess is to high or low for the grid size
while not correct:
    if (column_number > grid_size) or (column_number < 1): 
        new_column_number: int = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
        if 0 < new_column_number < grid_size:
            column_number = new_column_number
            correct = True
    else:
        correct = True

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


# grid output - comparing if the row or column number equal the secret ROW and COlUMN value
if (column_number == SECRET_COLUMN) and (row_number == SECRET_ROW):
    result = RED_BOX
    count_row = 1
    while count_row <= grid_size:
        grid = ""
        count_column = 1
        if row_number == count_row:
            while count_column <= grid_size: 
                if column_number == count_column:
                    grid += result
                else: 
                    grid += BLUE_BOX
                count_column += 1
            count_row += 1
        else: 
            while count_column <= grid_size:
                grid += BLUE_BOX
                count_column += 1
            count_row += 1
        print(grid)
    print("Hit!")
elif (row_number == SECRET_ROW) and (column_number != SECRET_COLUMN):
    result = WHITE_BOX
    count_row = 1
    while count_row <= grid_size:
        grid = ""
        count_column = 1
        if row_number == count_row:
            while count_column <= grid_size: 
                if column_number == count_column:
                    grid += result
                else: 
                    grid += BLUE_BOX
                count_column += 1
            count_row += 1
        else: 
            while count_column <= grid_size:
                grid += BLUE_BOX
                count_column += 1
            count_row += 1
        print(grid)
    print("Close! Correct row, wrong column.")
elif (column_number == SECRET_COLUMN) and (row_number != SECRET_ROW):
    result = WHITE_BOX
    count_row = 1
    while count_row <= grid_size:
        grid = ""
        count_column = 1
        if row_number == count_row:
            while count_column <= grid_size: 
                if column_number == count_column:
                    grid += result
                else: 
                    grid += BLUE_BOX
                count_column += 1
            count_row += 1
        else: 
            while count_column <= grid_size:
                grid += BLUE_BOX
                count_column += 1
            count_row += 1
        print(grid)
    print("Close! Correct column, wrong row.")
else:
    result = WHITE_BOX
    count_row = 1
    while count_row <= grid_size:
        grid = ""
        count_column = 1
        if row_number == count_row:
            while count_column <= grid_size: 
                if column_number == count_column:
                    grid += result
                else: 
                    grid += BLUE_BOX
                count_column += 1
            count_row += 1
        else: 
            while count_column <= grid_size:
                grid += BLUE_BOX
                count_column += 1
            count_row += 1
        print(grid)
    print("Miss!")