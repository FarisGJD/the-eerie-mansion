"""
The Haunted Mansion
By: Faris Dhoot
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
            print("Invalid entery, please select yes or no")


def third_floor():
    """"
    Starting game floor
    """
    slowprint("""There are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings scratched on to it and the
    \rthird has a strange liquid seeping through the bottom.""")
    user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

    # Main Winning Path
    if user_answer == 1:
        slowprint("""You enter and find an empty room with two doors on
        \reither side. The first looks ordinary and unassuming but the second
        \rhas a trail of tiny spiders walking towards and underneath the door.
        \rThey look as if they are heading towards something.""")
        user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

        # Instant Loosing Path
        if user_answer == 1:
            game_over("""AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
            \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMITING TO YOUR
            \rDEATH.""")

        # Continuing Winning Path
        elif user_answer == 2:
            slowprint("""You enter the second door to find a library of books
            \rcovered in dust and cobwebs. As you search through the
            \rliterature, you lift a book which is connected to a mechanism,
            \rrevealing a fake bookcase with three doors behind it.""")
            user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path
            if user_answer == 1:
                print(1)

            # Instant Loosing Path
            elif user_answer == 2:
                game_over("""INSTANT DEATH!!! YOU TRIGGER ANOTHER MECHANISIM
                \nTHAT SHOOTS AN ARROW STRAIGHT THROUGH YOUR HEAD. """)

            # Continuing Path
            elif user_answer == 3:
                print(3)

    # Loosing Path
    elif user_answer == 2:
        game_over("""YOU ENTER A ROOM WITH FLICKERING LIGHTING. YOU LOOK
        \rAROUND AND FIND A DESHEVLED MAN STANDING IN THE CORNER, HAUNTINGLY
        \rGLARING AT YOU..........OH NO!!! HE STARTS RUNNING TOWARDS YOU WITH A
        \rKNIFE IN HAND.""")

    # Secondary Winning Path
    elif user_answer == 3:
        print()


# def validation_checking(third_floor_answer):
#     """
#     Checks for errors made by user input and throws
#     relevant warning
#     """
#     try:
#         for num in range(1, 4):
#             if third_floor_answer != num:
#                 raise ValueError(
#                     (f"""Your answer should either be the number 1,2,3,
#                     you entered {third_floor_answer}""")
#                 )

#     except ValueError as error:
#         print(f"Invalid input: {error}, please try again. \n")
#         return False
#     return True


def game_over(text):
    """
    Informs the user that they have lost the game
    with an appropriate message
    """
    slowprint(f" ☠️☠️☠️☠️☠️☠️  {text} GAME OVER ☠️☠️☠️☠️☠️☠️")
    quit()


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    slowprint(""".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.
    \r.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")


def game_main():
    """
    Implements the games principle functions
    """
    start_game()
    third_floor()
    # validation_checking(user_answer)


slowprint("Welcome To The Haunted Mansion, Choose Your Own Adventure!")

game_main()
