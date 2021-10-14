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
    # Level Introduction
    slowprint("""There are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.""")
    user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

    # Main Winning Path
    if user_answer == 1:
        slowprint("""You enter and find an empty room with two doors on
        \reither side. The first looks ordinary and unassuming, however the
        \rsecond has a trail of tiny spiders walking towards and underneath
        \rthe door. They look as if they are heading towards something.""")
        user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

        # Instant Loosing Path
        if user_answer == 1:
            game_over("""AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
            \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMITING TO YOUR
            \rDEATH.""")

        # Continuing Winning Path
        elif user_answer == 2:
            slowprint("""You open the second door to find a library filled with
            \rbooks that are covered in dust and cobwebs. As you search
            \rthrough the literature, you lift a book which triggers a
            \rmechanism, revealing a fake bookcase with three doors behind it.
            \r""")
            user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path
            if user_answer == 1:
                slowprint("""As you enter the room part of the celling
                \rcollapses, trapping you inside. You look around to find a
                \rlone door in front of you and no alternate path. You have no
                \rchoice but to enter.\n""")

                slowprint("""Amid opening the door, you are stupefied by the
                \rodour of rotting corpses dissipating from within; though
                \rthere are no bodies to be found, the smell is so intense you
                \rcannot bare to stay a second longer. Quick there are two
                \rdoors in front of you""")

            # Instant Loosing Path
            elif user_answer == 2:
                game_over("""INSTANT DEATH!! THE PREVIOUS ROOMS MECHANISM
                \rTRIGGERS AN CROSS BOW AND ARROW, PIRCING STRAIGHT THROUGH
                \rYOUR SKULL.""")

            # Continuing Path
            elif user_answer == 3:
                slowprint("""You enter the room and find two doors side by
                \rside. The first has a blacked-out window next to it. You try
                \rand look through but cannot discern anything. As you
                \rscramble, desperate to gather your surroundings you find a
                \rtiny scratched off surface and look through. You realise you
                \rare three stories above a garden. You try to look for more
                \rclues and see what appears to be the beginnings of staircase
                \rhandle connected to the first door""")
                user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

                # Instant Loosing Path
                if user_answer == 1 or 2:
                    game_over("""AS YOU OPEN THE DOOR YOU FEEL A BREEZE
                    \rEMINATINMG FROM THE OTHER SIDE. EXITED YOU QUICKLY WALK
                    \rTHROUGH TO FIND THE STAIRCASE WAS A DECOY WITH NO STEPS.
                    \rYOU FALL DOWN THREE STOREIS TO YOUR DEATH.""")

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
