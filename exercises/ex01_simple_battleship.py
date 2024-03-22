"""EX01 Simple Battleship."""

__author__ = "730671755"

player_1_string: str = input("Pick a secret boat location between 1 and 4: ")
player_1_number: int = int(player_1_string)

if player_1_number > 4:
    print(f"Error! {player_1_string} too high!")
    quit()
else: 
    if player_1_number < 1:
        print(f"Error! {player_1_string} too low!")
        exit()

player_2_string: str = input("Guess a number between 1 and 4: ")
player_2_number: int = int(player_2_string)

if player_2_number > 4:
    print(f"Error! {player_2_string} too high!")
    quit()
else: 
    if player_2_number < 1:
        print(f"Error!  {player_2_string} too low!")
        quit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str = ""

if player_2_number == player_1_number:
    result = RED_BOX
    if player_2_number == 1:
        print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_number == 2:
        print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
    if player_2_number == 3:
        print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
    if player_2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
else:
    result = WHITE_BOX
    if player_2_number == 1:
        print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if player_2_number == 2:
        print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
    if player_2_number == 3:
        print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
    if player_2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)

if player_2_number == player_1_number:
    print("Correct! You hit the ship.")
else: 
    print("Incorrect! You missed the ship.")