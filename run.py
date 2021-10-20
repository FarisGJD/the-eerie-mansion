"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
import sys
import time
from path import p1_correct_path, p1_correct_path_additions, p1_losing_path, p2_losing_path 


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
        slowprint(p1_correct_path['p1'])
        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

        # Instant Losing Path
        if answer == 1:
            level_restart(p1_losing_path['p1'])

        # Continuing Winning Path (2)
        elif answer == 2:
            slowprint(p1_correct_path['p2'])
            answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

            # Continuing Winning Path (3)
            if answer == 1:
                slowprint(p1_correct_path['p3'])
                read_game_clue_files("assets/game-txt-files/game-clue-files/novel.txt", "novel")
                slowprint(p1_correct_path_additions['p3a'])
                answer = int(input("\nWhich Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if answer == 1:
                    level_restart(p1_losing_path['p2'])

                # Continuing Winning Path (4)
                elif answer == 2:
                    slowprint(p1_correct_path['p4'])
                    answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                    # Instant Losing Path
                    if answer == 1:
                        level_restart(p1_losing_path['p3'])

                    # Instant Losing Path
                    elif answer == 2:
                        level_restart(p1_losing_path['p4'])

                    # Continuing Winning Path (5)
                    elif answer == 3:
                        slowprint(p1_correct_path['p5'])
                        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                        # Instant Losing Path
                        if answer == 1:
                            level_restart(p1_losing_path['p5'])

                        # Continuing Winning Path (6)
                        elif answer == 2:
                            slowprint(p1_correct_path['p6'])
                            answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                            # Instant Losing Path
                            if answer == 1:
                                level_restart(p1_losing_path['p6'])

                            # Continuing Winning Path (7)
                            elif answer == 2:
                                slowprint(p1_correct_path['p7'])
                                read_game_clue_files("assets/game-txt-files/game-clue-files/greenhouse-report.txt", "report")
                                slowprint(p1_correct_path_additions['p7a'])
                                answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                                # Instant Losing Path
                                if answer == 1 or answer == 2:
                                    level_restart(p1_losing_path['p7'])

                                # Continuing Winning Path (8)
                                elif answer == 3:
                                    slowprint(p1_correct_path['p8'])
                                    answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                    # Continuing Winning Path (9)
                                    if answer == 1:
                                        slowprint(p1_correct_path['p9'])
                                        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                                        # Instant Losing Path
                                        if answer == 1:
                                            level_restart(p1_losing_path['p8'])

                                        # Continuing Winning Path (10)
                                        elif answer == 2:
                                            slowprint(p1_correct_path['p10'])

                                    # Instant Losing Path
                                    elif answer == 2:
                                        level_restart(p1_losing_path['p9'])

            # Instant Losing Path
            elif answer == 2:
                level_restart(p1_losing_path['p3ii'])

            # Continuing Path
            elif answer == 3:
                slowprint(p1_correct_path['p3i'])
                answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if answer == 1 or answer == 2:
                    level_restart(p1_losing_path['p3i'])

    # Primary Losing Path
    elif answer == 2:
        level_restart(p2_losing_path['p1'])

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
