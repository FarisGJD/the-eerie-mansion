"""
THE HAUNED MANSION BY FARIS DHOOT
"""

# Document imports
import sys
import time


def slowprint(slow):
    """
    Function that uses the sys & time modules to
    print text slow in the terminal
    """
    for slw in slow + '\n':
        sys.stdout.write(slw)
        sys.stdout.flush()
        time.sleep(0.5/10)


slowprint("Welcome To The Haunted Mansion, Choose Your Own Adventure!")


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input("Would you like to play (yes/no):\n").lower().strip()

        if playing == "yes":
            slowprint("Initialising Game.....................................")
            time.sleep(2)
            game_transition()
            break

        elif playing == "no":
            slowprint("Thanks for visiting, come back soon")
            quit()

        elif playing != "yes":
            slowprint("Invalid entery, please select yes or no")


def third_floor():
    """"
    Starting game floor
    """
    slowprint("There are three doors infront of you, the first is covered in")
    slowprint("cob webs, The second has peculiar markings on it and the third")
    slowprint("has a strange liquid seeping through the bottom which do you")
    slowprint("choose")

    user_answer = input("1, 2, 3\n").strip()
    if int(user_answer) == 1:
        print("""You enter the room and see several spiders and a door, do you
        enter?""")



# def validation_checking(third_floor_answer):
#     """
#     Checks for errors made by user input and throws
#     relevant warning
#     """
#     try:
#         [int(third_floor_answer) for value in third_floor_answer]
#         if third_floor_answer != 3:
#             raise ValueError(
#                 (f"""Your answer should either be yes or no,
#                  you entered {third_floor_answer}""")
#             )

#     except ValueError as error:
#         print(f"Invalid input: {error}, please try again. \n")


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    slowprint(""".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")
    slowprint(""".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")


def game_main():
    """
    Implements the games principle functions
    """
    start_game()
    third_floor()


game_main()
