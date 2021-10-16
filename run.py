"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
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
        time.sleep(0.3/10)


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input("Would you like to play (yes/no):\n").lower().strip()

        if playing == "yes":
            slowprint("\nInitialising Game")
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

    # Level Introduction
    slowprint("""\nThere are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.\n""")
    user_answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

    # Main Winning Path (Sequence 1|2|1|2|3|2|2|1|3|1) (1)
    if user_answer == 1:
        slowprint("""\nYou enter and find an empty room with two doors on
        \reither side. The first looks ordinary and unassuming, however the
        \rsecond has a trail of tiny spiders walking towards and underneath
        \rthe door. They look as if they are heading towards something.\n""")
        user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

        # Instant Losing Path
        if user_answer == 1:
            level_restart("""AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
            \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMMETING TO YOUR
            \rDEATH.""")

        # Continuing Winning Path (2)
        elif user_answer == 2:
            slowprint("""\nYou open the second door to find a library filled with
            \rbooks that are covered in dust and cobwebs. As you search
            \rthrough the literature, you lift a novel which triggers a
            \rmechanism, revealing a fake bookcase with three doors behind it.
            """)
            user_answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path (3)
            if user_answer == 1:
                slowprint("""\nAs you enter the room part of the celling
                \rcollapses, trapping you inside. You look around to find a
                \rlone door ahead of you with no alternate path. You have no
                \rchoice but to enter.\n""")

                slowprint("""Amid opening the door, you are stupefied by the
                \rodour of rotting corpses dissipating from within; though
                \rthere are no bodies to be found. The smell is so intense you
                \rcannot bare to stay a second longer. Quick there are two
                \rdoors in front of you\n""")
                user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if user_answer == 1:
                    level_restart("""YOU WALK INTO A BEDROOM THAT LOOKS RECENTLY
                    \rLIVED IN. THIS MEANS SOMEONE ELSE MIGHT BE NEARBY AND
                    \rABLE TO HELP. SUDDENLY YOU HEAR A LOUD THUD AND NOTICE A
                    \rCHANDELIER ABOVE YOU. IT SWIFTLY BECOMES UNDONE AND
                    \rFALLS ONTO YOU KNOCKING YOU OUT......AS YOU FALL IN AND
                    \rOUT OF CONSCIOUSNESS YOU NOTICE A DARK FIGURE STANDING
                    \rABOVE YOU WITH A NEEDLE IN HAND.""")

                # Continuing Winning Path (4)
                elif user_answer == 2:
                    slowprint("""\nYou open the door to find a long hallway
                    \rleading one direction, this looks promising. You start
                    \ryour journey trying to locate the end......It feels like
                    \ryou have been walking for hours. You finally reach a
                    \rcross roads which departs to three doors.\n""")
                    user_answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                    # Instant Losing Path
                    if user_answer == 1:
                        level_restart("""YOU ENTER A PITCH-BLACK ROOM AND ARE
                        \rUNABLE TO SEE. UNEXPECTEDLY THE LIGHTS TURN ON AND A
                        \rSWINGING GUILLOTINE SLICES YOU IN HALF.""")

                    # Instant Losing Path
                    elif user_answer == 2:
                        level_restart("""YOU WALK THROUGH THE DOOR AND ARE GREETED
                        \rWITHIN AN INCLINING PATH. AS YOU MAKE YOUR WAY
                        \rTHROUGH YOU HEAR A RUMBLING NOISE. YOU NOTICE AN
                        \rOBJECT HURTLING TOWARDS YOU. OH NO, IT’S A MASSIVE
                        \rBOULDER.""")

                    # Continuing Winning Path (5)
                    elif user_answer == 3:
                        slowprint("""\nAs you open the door you walk through a
                        \rthick layer of cobwebs. You see two doors, the first
                        \rlooks untouched while the second appears to be
                        \rcovered in fang marks.\n""")
                        user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                        # Instant Losing Path
                        if user_answer == 1:
                            level_restart("\nYOU REACH A DEAD END WITH NO WAY OUT.")

                        # Continuing Winning Path (6)
                        elif user_answer == 2:
                            slowprint("""\nYou walk into an icy, cold room. As
                            \ryou look around your breath starts to produce
                            \rcondensation due to the extreme temperature. You
                            \rsee two doors both looking ordinary. As you
                            \rclosely inspect them you find the handle of the
                            \rsecond door to be covered in dry blood.\n""")
                            user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                            # Instant Losing Path
                            if user_answer == 1:
                                level_restart("""YOU ENTER A ROOM COVERED IN GREEN
                                \rSMOKE. AS SOON AS YOU TAKE A BREATH YOU
                                \rCOLLAPSE AND LOSE CONSCIOUSNESS.""")

                            # Continuing Winning Path (7)
                            elif user_answer == 2:
                                slowprint("""\nYou enter the room, shocked and
                                \rhorrified by what you see. Several silk
                                \rcocoons, blood and human remains are
                                \rscattered throughout. As you try to exit
                                \rfrom where you entered, a spider web shoots
                                \rfrom above you, blocking the door. You look
                                \rup to see a massive spider. Quick there are
                                \rthree doors in front of you.\n""")
                                user_answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                                # Instant Losing Path
                                if user_answer == 1 or user_answer == 2:
                                    level_restart("""AS YOU WALK INSIDE YOU
                                    \rNOITCE THAT THE FLOOR IS FLOODED AND
                                    \rCONNECTED TO THE NEIGHBOURING ROOM. YOU
                                    \rBEGIN TO WALK TO THE ONLY DOOR INFRONT
                                    \rOF YOU. ALL THE SUDDEN A LOOSE, ACTIVE
                                    \rWIRE FALLS TO THE GROUND ELECTROCUTING
                                    \rYOU.""")

                                # Continuing Winning Path (8)
                                elif user_answer == 3:
                                    slowprint("""\nYou enter to see a massive
                                    \rgreenhouse sheltering large exotic
                                    \rplants. As you walk through you hear
                                    \rscuttering all around you.\n""")
                                    user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                    if user_answer == 1:
                                        slowprint("""\nYou enter a room to find
                                        \rheaps of spider eggs and
                                        \rexoskeletons bigger than the spider
                                        \ryou encountered before. You see two
                                        \rdoors both with a strange clear
                                        \rsubstance on them. As you touch and
                                        \rinspect it your hand starts to burn.
                                        \rCould it be venom?\n""")
                                        user_answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                        if user_answer == 1:
                                            level_restart("""YOU WALK INTO A DARK ROOM,
                                            \rBARELY ABLE TO SEE. YOU DELVE
                                            \rDEEPER INTO THE SPACE, TRYING TO
                                            \rFEEL FOR ANYTHING FAMILIAR. BY A
                                            \rSTROKE OF LUCK, YOU FIND A LIGHT
                                            \rSWITCH ATTACHED TO THE
                                            \rWALL. YOU TURN ON THE LIGHT......
                                            \rAND FIND YOURSELF SURROUNDED BY
                                            \rTHOUSANDS OF TINY SPIDERS,
                                            \rINSTANTLY ATTACKING YOU.""")

                                        elif user_answer == 1:
                                            slowprint("""As you walk in you
                                            \rhear deafening hissing noises
                                            \rcoming from the only door ahead
                                            \rof you. Scared, you think of
                                            \rheading back but realise this is
                                            \rthe only way out. You take a
                                            \rdeep breath and open the door.OH
                                            \rNO!!! IT IS A COLOSSAL TARANTULA
                                            \rTHE SIZE OF A HOUSE. It notices
                                            \ryou and heads straight towards
                                            \rou. Panicked you try to run back
                                            \rbut it shoots venom outs its
                                            \rfans, collapsing the entire will
                                            \rand exit behind you. You brace
                                            \ryourself, thinking you have met
                                            \ryour impending doom.
                                            \rNext door.""")

                                    elif user_answer == 2:
                                        level_restart("""YOU WALK INTO A TRAP
                                        \rAND FALL INTO A WATER HOLE. YOU'RE
                                        \rNOT ALONE. SUDDENLY YOU FEEL
                                        \rSOMETHING BITING YOUR LEG, DRAGGING
                                        \rYOU UNDER. IT'S AN ALLIGATOR. YOU TRY
                                        \rTO ESCAPE ITS GRIP BUT ARE UNABLE TO
                                        \rMANOEUVRE OUT ITS DEATH ROLL.""")

            # Instant Losing Path
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
                user_answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                # Instant Losing Path
                if user_answer == 1 or user_answer == 2:
                    level_restart("""AS YOU OPEN THE DOOR YOU FEEL A BREEZE
                    \rEMANATING FROM THE OTHER SIDE. EXITED YOU QUICKLY WALK
                    \rTHROUGH TO FIND THE STAIRCASE WAS A DECOY WITH NO STEPS.
                    \rYOU FALL DOWN THREE STOREIS TO YOUR DEATH.""")

    # Primary Losing Path
    elif user_answer == 2:
        level_restart("""YOU ENTER A ROOM WITH FLICKERING LIGHTING. YOU LOOK
        \rAROUND AND FIND A DISHEVELLED MAN STANDING IN THE CORNER, HAUNTINGLY
        \rGLARING AT YOU..........OH NO!!! HE STARTS RUNNING TOWARDS YOU WITH A
        \rKNIFE IN HAND.""")

    # Secondary Losing Path
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
    the third_floor function or exits the game.
    """
    slowprint(f"\n⛔️⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} RESTARTING LEVEL ⛔️⛔️⛔️⛔️⛔️⛔️")
    while True:
        gameplay_choice = input("Would you like to continue with the adventure? Type: | yes | no |\n").lower().strip()

        if gameplay_choice == "yes":
            third_floor()
            break

        elif gameplay_choice == "no":
            slowprint("Thanks for visiting, come back soon")
            quit()

        elif gameplay_choice != "yes":
            slowprint("Invalid entery, please select yes or no")

    time.sleep(2)
    game_transition()


def game_over(text):
    """
    Informs the user that they have lost the game,
    restarting the programme.
    """
    slowprint(f"\n☠️☠️☠️☠️☠️☠️{text} GAME OVER☠️☠️☠️☠️☠️☠️")
    exit()


def read_text_files(game_file):
    """
    Accssesses game rules and stories
    """
    file = open(game_file, "r")
    text = file.read()
    file.close()
    slowprint(text)


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
    read_text_files("assets/game-rules-and-story-files/game-story.txt")
    time.sleep(2)
    game_transition()
    third_floor()
    # validation_checking(user_answer)


slowprint("Welcome To The Haunted Mansion, Choose Your Own Adventure!\n")
game_main()
