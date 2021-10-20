"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
import sys
import time
from path import correct_path


def slowprint(slow):
    """
    Function that uses the sys & time modules to
    print text slow in the terminal
    """
    for slw in slow + '\n':
        sys.stdout.write(slw)
        sys.stdout.flush()
        time.sleep(0.0000000003/10)


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input("Do you dare play? Type: | yes | no |\n").lower().strip()

        if playing == "yes":
            slowprint("\nInitialising Game")
            # time.sleep(2)
            game_transition()
            break

        elif playing == "no":
            slowprint("\nThanks for visiting, come back soon")
            quit()

        elif playing != "yes":
            slowprint("\nInvalid entery, please select yes or no")


def third_floor():
    """"
    Starting game floor
    """

    # Level Introduction
    slowprint("""\nThere are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.\n""")
    answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

    # Main Winning Path (Sequence 1|2|1|2|3|2|2|3|1|2)
    if answer == 1:
        slowprint(correct_path['p1'])
        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

        # Instant Losing Path
        if answer == 1:
            level_restart("""AS YOU OPEN THE DOOR YOU IMMEDIATELY START FALLING,
            \rREALISING THE FLOOR WAS COMPLETELY MISSING, PLUMMETING TO YOUR
            \rDEATH.""")

        # Continuing Winning Path (2)
        elif answer == 2:
            slowprint(correct_path['p2'])
            # slowprint("""\nYou open the second door to find a library filled with
            # \rbooks that are covered in dust and cobwebs. As you search
            # \rthrough the literature, you lift a biographic novel\n""")
            # read_game_clue_files("assets/game-txt-files/game-clue-files/novel.txt", "novel")
            # slowprint("""\nLifting the novel triggers a mechanism,
            # \rrevealing a fake bookcase with three doors behind it.\n""")
            answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path (3)
            if answer == 1:
                slowprint("""\nAs you enter the room part of the celling
                \rcollapses, trapping you inside. You look around to find a
                \rlone door ahead of you with no way back or alternate path.
                \rYou have no choice but to enter.\n""")

                slowprint("""Amid opening the door, you are stupefied by the
                \rodour of rotting corpses dissipating from within; though
                \rthere are no bodies to be found. The smell is so intense you
                \rcannot bare to stay a second longer. Quick there are two
                \rdoors in front of you.\n""")
                answer = int(input("\nWhich Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if answer == 1:
                    level_restart("""YOU WALK INTO A BEDROOM THAT LOOKS RECENTLY
                    \rLIVED IN. THIS MEANS SOMEONE ELSE MIGHT BE NEARBY AND
                    \rABLE TO HELP. SUDDENLY YOU HEAR A LOUD THUD AND NOTICE A
                    \rCHANDELIER ABOVE YOU. IT SWIFTLY BECOMES UNDONE AND
                    \rFALLS ONTO YOU KNOCKING YOU OUT......AS YOU FALL IN AND
                    \rOUT OF CONSCIOUSNESS YOU NOTICE A DARK FIGURE STANDING
                    \rABOVE YOU WITH A NEEDLE IN HAND.""")

                # Continuing Winning Path (4)
                elif answer == 2:
                    slowprint("""\nYou open the door to find a long hallway
                    \rleading one direction, this looks promising. You start
                    \ryour journey trying to locate the end......It feels like
                    \ryou have been walking for hours. You finally reach a
                    \rcross roads which departs to three doors.\n""")
                    answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                    # Instant Losing Path
                    if answer == 1:
                        level_restart("""YOU ENTER A PITCH-BLACK ROOM AND ARE
                        \rUNABLE TO SEE. UNEXPECTEDLY THE LIGHTS TURN ON AND A
                        \rSWINGING GUILLOTINE SLICES YOU IN HALF.""")

                    # Instant Losing Path
                    elif answer == 2:
                        level_restart("""YOU WALK THROUGH THE DOOR AND ARE GREETED
                        \rWITHIN AN INCLINING PATH. AS YOU MAKE YOUR WAY
                        \rTHROUGH YOU HEAR A RUMBLING NOISE. YOU NOTICE AN
                        \rOBJECT HURTLING TOWARDS YOU. OH NO, IT’S A MASSIVE
                        \rBOULDER.""")

                    # Continuing Winning Path (5)
                    elif answer == 3:
                        slowprint("""\nAs you open the door you walk through a
                        \rthick layer of cobwebs. You see two doors, the first
                        \rlooks untouched while the second appears to be
                        \rcovered in fang marks.\n""")
                        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                        # Instant Losing Path
                        if answer == 1:
                            level_restart("\nYOU REACH A DEAD END WITH NO WAY OUT.")

                        # Continuing Winning Path (6)
                        elif answer == 2:
                            slowprint("""\nYou walk into an icy, cold room. As
                            \ryou look around your breath starts to produce
                            \rcondensation due to the extreme temperature. You
                            \rsee two doors both looking ordinary. As you
                            \rclosely inspect them you find the handle of the
                            \rsecond door to be covered in dry blood.\n""")
                            answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                            # Instant Losing Path
                            if answer == 1:
                                level_restart("""YOU ENTER A ROOM COVERED IN GREEN
                                \rSMOKE. AS SOON AS YOU TAKE A BREATH YOU
                                \rCOLLAPSE AND LOSE CONSCIOUSNESS.""")

                            # Continuing Winning Path (7)
                            elif answer == 2:
                                slowprint("""\nYou enter the room, shocked and
                                \rhorrified by what you see. Several silk
                                \rcocoons, blood and human remains are
                                \rscattered throughout. As you try to exit
                                \rfrom where you entered, a spider web shoots
                                \rfrom above you, blocking the door. You look
                                \rup to see a massive spider. Quick there are
                                \rthree doors in front of you.\n""")
                                answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                                # Instant Losing Path
                                if answer == 1 or answer == 2:
                                    level_restart("""AS YOU WALK INSIDE YOU
                                    \rNOITCE THAT THE FLOOR IS FLOODED AND
                                    \rCONNECTED TO THE NEIGHBOURING ROOM. YOU
                                    \rBEGIN TO WALK TO THE ONLY DOOR INFRONT
                                    \rOF YOU. ALL THE SUDDEN A LOOSE, ACTIVE
                                    \rWIRE FALLS TO THE GROUND ELECTROCUTING
                                    \rYOU.""")

                                # Continuing Winning Path (8)
                                elif answer == 3:
                                    slowprint("""\nYou enter to see a massive
                                    \rgreenhouse sheltering large exotic
                                    \rplants. As you walk through you hear
                                    \rscuttering all around you. You find a
                                    \rpeice of paper titled "Experiment Report,
                                    \rBy Dr. Charles Falken"\n""")
                                    read_game_clue_files("assets/game-txt-files/game-clue-files/greenhouse-report.txt", "report")
                                    slowprint("""\nYou finish reading the
                                    \rreport and realise you are being watched
                                    \rby hunderds of spiders surrounding you.
                                    \rDon’t make any sudden movements. Quick
                                    \rthere are two doors in front of
                                    \ryou.\n""")
                                    answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                    # Continuing Winning Path (9)
                                    if answer == 1:
                                        slowprint("""\nYou enter a room to find
                                        \rheaps of spider eggs and
                                        \rexoskeletons bigger than the spider
                                        \ryou encountered before. You see two
                                        \rdoors both with a strange clear
                                        \rsubstance on them. As you touch and
                                        \rinspect it your hand starts to burn.
                                        \rCould it be venom?\n""")
                                        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                        # Instant Losing Path
                                        if answer == 1:
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

                                        # Continuing Winning Path (10)
                                        elif answer == 2:
                                            slowprint("""As you walk in you
                                            \rhear a deafening hissing noise
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

                                    # Instant Losing Path
                                    elif answer == 2:
                                        level_restart("""YOU WALK INTO A TRAP
                                        \rAND FALL INTO A WATER HOLE. YOU'RE
                                        \rNOT ALONE. SUDDENLY YOU FEEL
                                        \rSOMETHING BITING YOUR LEG, DRAGGING
                                        \rYOU UNDER. IT'S AN ALLIGATOR. YOU TRY
                                        \rTO ESCAPE ITS GRIP BUT ARE UNABLE TO
                                        \rMANOEUVRE OUT ITS DEATH ROLL.""")

            # Instant Losing Path
            elif answer == 2:
                level_restart("""THE PREVIOUS ROOMS MECHANISM TRIGGERS, A
                \rCROSSBOW AND ARROW, PIERCING STRAIGHT THROUGH
                \rYOUR SKULL.""")

            # Continuing Path
            elif answer == 3:
                slowprint("""\nYou enter the room and find two doors side by
                \rside. The first has a blacked-out window next to it. You try
                \rand look through but cannot discern anything. As you
                \rscramble, desperate to gather your surroundings you find a
                \rtiny scratched off surface and look through. You realise you
                \rare three stories above a garden. You try to look for more
                \rclues and see what appears to be the beginnings of staircase
                \rhandle connected to the first door.\n""")
                answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if answer == 1 or answer == 2:
                    level_restart("""AS YOU OPEN THE DOOR YOU FEEL A BREEZE
                    \rEMANATING FROM THE OTHER SIDE. EXITED YOU QUICKLY WALK
                    \rTHROUGH TO FIND THE STAIRCASE WAS A DECOY WITH NO STEPS.
                    \rYOU FALL DOWN THREE STOREIS TO YOUR DEATH.""")

    # Primary Losing Path
    elif answer == 2:
        level_restart("""YOU ENTER A ROOM WITH FLICKERING LIGHTING. YOU LOOK
        \rAROUND AND FIND A DISHEVELLED MAN STANDING IN THE CORNER, HAUNTINGLY
        \rGLARING AT YOU..........OH NO!!! HE STARTS RUNNING TOWARDS YOU WITH A
        \rKNIFE IN HAND, SCREAMING SPIDERS! SPIDERS!.""")

    # Secondary Losing Path (Sequence | 3 | 2 | 1 | 2 |)
    elif answer == 3:
        slowprint("""\nAs you enter the room you start to feel your feet
        \rburning. You look down and see smoke arising from your shoes. You
        \rrealise the clear liquid is some sort of corrosive substance. You
        \rquickly take your shoes off before it starts to burn you skin. There
        \rare three doors in front of you.\n""")
        answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

        if answer == 1:
            level_restart("""YOU ENTER THE ROOM AND ARE ATTACKED BY A MURDER
            \rOF CROWS. THEY START PECKING AT YOUR FLESH AS YOU ARE UNABLE TO
            \rSTOP THEM.""")

        elif answer == 2:
            level_restart("""AS YOU OPEN THE DOOR YOU ARE BOMBARDED BY A WAVE
            \rOF THE CARROSIVE SUBSTANCE. AS IT BEGINS TO EAT AT YOUR FLESH, A
            \rNOTE DRIFTS TOWARDS YOU THAT SAYS “Spider Venom”.""")

        elif answer == 3:
            slowprint("""\nYou walk into the room and see several pieces of paper
            \rscattered across the floor. You pick one up titled “Experiment
            \rNotes”. You try to read the rest but cannot make sense of its
            \rscientific content. There are two doors in front of you.\n""")
            answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

            if answer == 1:
                level_restart("""YOU WALK IN AND ARE IMMEDIATELY INTERCEPTED
                \rBY AN ABNORMALY LARGE ANACONDA. IT STARTS TO WRAP AROUND YOU,
                \rENGULFING YOU ITS MOTUH.""")

            elif answer == 2:
                slowprint("""\nYou walk into a space with a sign that says
                \r“Holding Room”. You are surrounded by hazmat suits. Things
                \rare getting strange. There are two doors in front of
                \ryou.\n""")
                answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                if answer == 1:
                    slowprint("""\nYou enter another holding room, but this time
                    \rsurrounded by various medical equipment and empty
                    \rbattered cages. You look around and find more of the
                    \rspider venom in vials labelled “CHEMICAL X”. Things are
                    \rdefinitely getting strange. There are two doors in front
                    \rof you.\n""")
                    answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                    if answer == 1:
                        level_restart("""YOU ENTER THE ROOM AND FIND SEVERAL
                        \rMONKYS SCREAMING IN AGONY. THE LONGER YOU LOOK THE
                        \rMORE YOU REALISE THESE ARENT NORMAL MONKIES.  THEY
                        \rSEEM TO HAVE BEEN GENETICALLY ENGINEERED WITH SOME
                        \rOTHER CREATURE. ONE OF THEM NOTICES AND CHARGES AT
                        \rYOU.""")

                    elif answer == 2:
                        slowprint("""\nAs you attempt to open the door you
                        \rrealise something is different. The door is
                        \rextremely heavy. You use all your strength to prize
                        \rit open. As you walk inside the door swiftly shuts
                        \rand locks behind you. You look back and realise it
                        \ris some kind of vault, hooked to a mechanism, making
                        \rsure nothing inside got out. You see three of the
                        \rsame doors ahead.\n""")
                        answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                        if answer == 1 or answer == 2 or answer == 3:
                            slowprint("""\nYou enter the room to hear a
                            \rrobotic voice speaking – “ALERT! ALERT!
                            \rEXPERIMENT 626 HAS ESCAPED” and red flashing
                            \rlights. As you look around you realise you are
                            \rin a laboratory. You find several Hybrid
                            \rcreatures attached to machines screaming in
                            \ragony. You find a book titled “Chimera”.\n""")
                            read_game_clue_files("assets/game-txt-files/game-clue-files/lab-book.txt", "book")
                            level_restart("""AS YOU PUT THE BOOK DOWN YOU FEEL
                            \rA TAP ON YOUR SHOULDER. YOU LOOK BACK STARTLED
                            \rTO FIND A HALF MAN HALF SPIDER HYBRID STARING AT
                            \rYOU WITH GLEE. BEFORE YOU COULD EVEN THINK YOU
                            \rARE IMMEDIATELY INJECTED WITH CHEMICAL X.""")

                elif answer == 2:
                    level_restart("""YOU ENTER THE ROOM AND FIND A TELEPHONE.
                    \rEXITED, YOU RUN TOWARDS IT AND CALL 999. SUCCESS IT
                    \rRINGS. YOU BEGIN TO DESCRIBE YOUR CIRCUMSTANCE TO THE
                    \rOPERATOR WHO REASSURES YOU. THEY ASK FOR YOU TO STAY ON
                    \rTHE LINE WHILE THEY TRACK YOUR LOCATION. SUDDENLY YOU
                    \rHEAR A LOUD GROWLING NOISE BEHIND YOU. IT’S A MASSIVE
                    \rTIGER.""")


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
    Takes the user back to the introductory path of
    its respective floor or exits the game.
    """
    slowprint(f"\n⛔️⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} RESTARTING LEVEL ⛔️⛔️⛔️⛔️⛔️⛔️")
    while True:
        gameplay_choice = input("\nWould you like to continue with the adventure?: | yes | no |\n").lower().strip()

        if gameplay_choice == "yes":
            third_floor()
            break

        elif gameplay_choice == "no":
            slowprint("\nThanks for visiting, come back soon")
            quit()

        elif gameplay_choice != "yes":
            slowprint("\nIncorrect input, please select yes or no")

    # time.sleep(2)
    game_transition()


def game_over(text):
    """
    Informs the user that they have lost the game,
    restarting the programme.
    """
    slowprint(f"\n☠️☠️☠️☠️☠️☠️{text} GAME OVER☠️☠️☠️☠️☠️☠️")
    exit()


def read_game_intro_files(intro_file, text):
    """
    Reads game introductory files
    """
    while True:
        rules_file_answer = input(f"\nWould you like to read the {text}? Choose: | yes | no |\n").lower().strip()

        if rules_file_answer == "yes":
            with open(intro_file) as file:
                choice_text = file.read()
                slowprint(choice_text)
                continue_after_text()
                break

        elif rules_file_answer == "no":
            game_transition()
            break

        elif rules_file_answer != "yes":
            slowprint("\nInvalid entery, please select yes or no")


def read_game_clue_files(clue_file, text):
    """
    Reads the games clues and path choice
    files
    """
    while True:
        clues = input(f"Would you like to read the {text}? Choose: | yes | no |\n").lower().strip()

        if clues == "yes":
            with open(clue_file) as file:
                text = file.read()
                slowprint(text)
                continue_after_text()
                break

        elif clues == "no":
            break

        elif clues != "yes":
            slowprint("\nInvalid entery, please select yes or no")


def continue_after_text():
    """
    Allows user time to read game files
    then gives them the option to continue
    """
    while True:
        progress = input("\nClick 'c' and enter on your kerboard to continue\n").lower().strip()

        if progress == "c":
            break

        elif progress != "c":
            print("Invalid entery, please select the 'c' key")


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    slowprint("""\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.
    \r\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")


def game_main():
    """
    Implements the games principle functions
    """
    start_game()
    read_game_intro_files("assets/game-txt-files/game-intro-files/game-rules.txt", "rules")
    game_transition()
    read_game_intro_files("assets/game-txt-files/game-intro-files/game-plot.txt", "plot")
    game_transition()
    third_floor()
    # validation_checking(answer)


slowprint("\n☠️☠️☠️☠️☠️☠️ WELCOME TO THE EERIE MANSION, CHOOSE YOUR OWN ADVENTURE ☠️☠️☠️☠️☠️☠️\n")
game_main()
