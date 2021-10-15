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
            slowprint("\nInitialising Game...................................")
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
    slowprint("""\nThere are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.\n""")
    user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

    # Main Winning Path (Sequence 1|2|1|2|3|2|2|1|3|2)
    if user_answer == 1:
        slowprint("""\nYou enter and find an empty room with two doors on
        \reither side. The first looks ordinary and unassuming, however the
        \rsecond has a trail of tiny spiders walking towards and underneath
        \rthe door. They look as if they are heading towards something.\n""")
        user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

        # Instant Loosing Path
        if user_answer == 1:
            level_restart("""AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
            \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMMETING TO YOUR
            \rDEATH.""")

        # Continuing Winning Path
        elif user_answer == 2:
            slowprint("""\nYou open the second door to find a library filled with
            \rbooks that are covered in dust and cobwebs. As you search
            \rthrough the literature, you lift a novel which triggers a
            \rmechanism, revealing a fake bookcase with three doors behind it.
            """)
            user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path
            if user_answer == 1:
                slowprint("""\nAs you enter the room part of the celling
                \rcollapses, trapping you inside. You look around to find a
                \rlone door ahead of you with no alternate path. You have no
                \rchoice but to enter.\n""")

                slowprint("""\nAmid opening the door, you are stupefied by the
                \rodour of rotting corpses dissipating from within; though
                \rthere are no bodies to be found. The smell is so intense you
                \rcannot bare to stay a second longer. Quick there are two
                \rdoors in front of you\n""")
                user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

                # Instant Loosing Path
                if user_answer == 1:
                    level_restart("""YOU WALK INTO A BEDROOM THAT LOOKS RECENTLY
                    \rLIVED IN. THIS MEANS SOMEONE ELSE MIGHT BE NEARBY AND
                    \rABLE TO HELP. SUDDENLY YOU HEAR A LOUD THUD AND NOTICE A
                    \rCHANDELIER ABOVE YOU. IT SWIFTLY BECOMES UNDONE AND
                    \rFALLS ONTO YOU KNOCKING YOU OUT......AS YOU FALL IN AND
                    \rOUT OF CONSCIOUSNESS YOU NOTICE A DARK FIGURE STANDING
                    \rABOVE YOU WITH A NEEDLE IN HAND.""")

                # Continuing Winning Path
                elif user_answer == 2:
                    slowprint("""\nYou open the door to find a long hallway
                    \rleading one direction, this looks promising. You start
                    \ryour journey trying to locate the end......It feels like
                    \ryou have been walking for hours. You finally reach a
                    \rcross roads which departs to three doors\n""")
                    user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

                    # Instant Loosing Path
                    if user_answer == 1:
                        level_restart("""YOU ENTER A PITCH-BLACK ROOM AND ARE
                        \rUNABLE TO SEE. UNEXPECTEDLY THE LIGHTS TURN ON AND A
                        \rSWINGING GUILLOTINE SLICES YOU IN HALF.""")

                    # Instant Loosing Path
                    elif user_answer == 2:
                        level_restart("""YOU WALK THROUGH THE DOOR AND ARE GREETED
                        \rWITHIN AN INCLINING PATH. AS YOU MAKE YOUR WAY
                        \rTHROUGH YOU HEAR A RUMBLING NOISE. YOU NOTICE AN
                        \rOBJECT HURTLING TOWARDS YOU. OH NO, IT’S A MASSIVE
                        \rBOULDER.""")

                    # Continuing Winning Path
                    elif user_answer == 3:
                        slowprint("""\nAs you open the door you walk through a
                        \rthick layer of cobwebs. You see two doors, the first
                        \rlooks untouched while the second appears to be
                        \rcovered in fang marks.\n""")
                        user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

                        # Instant Loosing Path
                        if user_answer == 1:
                            level_restart("\nYOU REACH A DEAD END WITH NO WAY OUT.")

                        # Continuing Winning Path
                        elif user_answer == 2:
                            slowprint("""\nYou walk into an icy, cold room. As
                            \ryou look around your breath starts to produce
                            \rcondensation due to the extreme temperature. You
                            \rsee two doors both looking ordinary. As you
                            \rclosely inspect them you find the handle of the
                            \rsecond door to be covered in dry blood.\n""")
                            user_answer = int(input("Which Door Do You Enter:| 1 | 2 |\n").strip())

                            if user_answer == 1:
                                print("")

                            elif user_answer == 2:
                                level_restart("""\nYOU ENTER A ROOM COVERED IN GREEN
                                \rSMOKE. AS SOON AS YOU TAKE A BREATH YOU
                                \rCOLLAPSE AND LOSE CONSCIOUSNESS.""")

            # Instant Loosing Path
            elif user_answer == 2:
                level_restart("""THE PREVIOUS ROOMS MECHANISM TRIGGERS AN
                \rCROSSBOW AND ARROW, PIERCING STRAIGHT THROUGH
                \rYOUR SKULL.""")

            # Continuing Path
            elif user_answer == 3:
                slowprint("""\nYou enter the room and find two doors side by
                \rside. The first has a blacked-out window next to it. You try
                \rand look through but cannot discern anything. As you
                \rscramble, desperate to gather your surroundings you find a
                \rtiny scratched off surface and look through. You realise you
                \rare three stories above a garden. You try to look for more
                \rclues and see what appears to be the beginnings of staircase
                \rhandle connected to the first door\n""")
                user_answer = int(input("Which Door Do You Enter:| 1 | 2 | 3 |\n").strip())

                # Instant Loosing Path
                if user_answer == 1 or 2:
                    level_restart("""AS YOU OPEN THE DOOR YOU FEEL A BREEZE
                    \rEMANATING FROM THE OTHER SIDE. EXITED YOU QUICKLY WALK
                    \rTHROUGH TO FIND THE STAIRCASE WAS A DECOY WITH NO STEPS.
                    \rYOU FALL DOWN THREE STOREIS TO YOUR DEATH.""")

    # Primary Loosing Path
    elif user_answer == 2:
        level_restart("""YOU ENTER A ROOM WITH FLICKERING LIGHTING. YOU LOOK
        \rAROUND AND FIND A DISHEVELLED MAN STANDING IN THE CORNER, HAUNTINGLY
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


def level_restart(text):
    """
    Take the user back to the introductory path of
    the third_floor function
    """
    slowprint(f"\n⛔️⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} LEVEL RESTART ⛔️⛔️⛔️⛔️⛔️⛔️")


def game_over(text):
    """
    Informs the user that they have lost the game,
    restarting the programme.
    """
    slowprint(f"\n☠️☠️☠️☠️☠️☠️{text} GAME OVER☠️☠️☠️☠️☠️☠️")
    exit()


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


slowprint("Welcome To The Haunted Mansion, Choose Your Own Adventure!\n")

game_main()
