"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
import sys
import time
from path import p1_correct_path, p1_correct_path_additions, p1_losing_path, \
    p2_losing_path, p3_game_path, p3_losing_path
from functions import handel_game, questions_and_answers1


def slowprint(slow):
    """
    Function that uses the sys & time modules to
    print text slow in the terminal
    """
    for slw in slow + '\n':
        sys.stdout.write(slw)
        sys.stdout.flush()
        time.sleep(0.0000000000003/10)


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
            level_restart3(p1_losing_path['p1'])

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
                    level_restart3(p1_losing_path['p2'])

                # Continuing Winning Path (4)
                elif answer == 2:
                    slowprint(p1_correct_path['p4'])
                    answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                    # Instant Losing Path
                    if answer == 1:
                        level_restart3(p1_losing_path['p3'])

                    # Instant Losing Path
                    elif answer == 2:
                        level_restart3(p1_losing_path['p4'])

                    # Continuing Winning Path (5)
                    elif answer == 3:
                        slowprint(p1_correct_path['p5'])
                        answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                        # Instant Losing Path
                        if answer == 1:
                            level_restart3(p1_losing_path['p5'])

                        # Continuing Winning Path (6)
                        elif answer == 2:
                            slowprint(p1_correct_path['p6'])
                            answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                            # Instant Losing Path
                            if answer == 1:
                                level_restart3(p1_losing_path['p6'])

                            # Continuing Winning Path (7)
                            elif answer == 2:
                                slowprint(p1_correct_path['p7'])
                                read_game_clue_files("assets/game-txt-files/game-clue-files/greenhouse-report.txt", "report")
                                slowprint(p1_correct_path_additions['p7a'])
                                answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                                # Instant Losing Path
                                if answer == 1 or answer == 2:
                                    level_restart3(p1_losing_path['p7'])

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
                                            level_restart3(p1_losing_path['p8'])

                                        # Continuing Winning Path (10)
                                        elif answer == 2:
                                            slowprint(p1_correct_path['p10'])
                                            continue_after_text()

                                    # Instant Losing Path
                                    elif answer == 2:
                                        level_restart3(p1_losing_path['p9'])

            # Instant Losing Path
            elif answer == 2:
                level_restart3(p1_losing_path['p3ii'])

            # Continuing Path
            elif answer == 3:
                slowprint(p1_correct_path['p3i'])
                answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                # Instant Losing Path
                if answer == 1 or answer == 2:
                    level_restart3(p1_losing_path['p3i'])

    # Primary Losing Path
    elif answer == 2:
        level_restart3(p2_losing_path['p1'])

    # Secondary Losing Path (Sequence | 3 | 2 | 1 | 2 |)
    elif answer == 3:
        slowprint(p3_game_path["p1"])
        answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

        if answer == 1:
            level_restart3(p3_losing_path["p1"])

        elif answer == 2:
            level_restart3(p3_losing_path["p1i"])

        elif answer == 3:
            slowprint(p3_game_path["p2"])
            answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

            if answer == 1:
                level_restart3(p3_losing_path["p2"])

            elif answer == 2:
                slowprint(p3_game_path["p3"])
                answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                if answer == 1:
                    slowprint(p3_game_path["p4"])
                    answer = int(input("Which Door Do You Enter: | 1 | 2 |\n").strip())

                    if answer == 1:
                        level_restart3(p3_losing_path["p3"])

                    elif answer == 2:
                        slowprint(p3_game_path["p5"])
                        answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())

                        if answer == 1 or answer == 2 or answer == 3:
                            slowprint(p3_game_path["p6"])
                            read_game_clue_files("assets/game-txt-files/game-clue-files/lab-book.txt", "book")
                            level_restart3(p3_losing_path["p5"])

                elif answer == 2:
                    level_restart3(p3_losing_path["p4"])


def second_floor():
    """
    Second Game Floor
    """
    slowprint("""\nBefore arriving to the end of the stairs you reach a balcony.
    \rBeneath you is a mind filed of traps and strange doors with markings on
    \rthem. You approach the first set of 3 doors.\n""")
    answer2 = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip())

    if answer2 == 1:
        level_restart2()

    elif answer2 == 2:
        slowprint("You read the strange markings on the door")
        handel_game(questions_and_answers1)

    elif answer2 == 3:
        level_restart2()


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


def level_restart3(text):
    """
    Takes user back to the begning of
    the third floor
    """
    slowprint(f"\n⛔️⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} RESTARTING LEVEL ⛔️⛔️⛔️⛔️⛔️⛔️")
    while True:
        level3_choice = input("\nWould you like to continue with the adventure?: | yes | no |\n").lower().strip()

        if level3_choice == "yes":
            third_floor()
            break

        elif level3_choice == "no":
            slowprint("\nThanks for visiting, come back soon")
            # time.sleep(2)
            game_transition()
            quit()

        elif level3_choice != "yes":
            slowprint("\nIncorrect input, please select yes or no")


def level_restart2():
    """
    Takes user back to the begning of
    the second floor
    """
    slowprint("\n❌❌❌❌❌❌ INCORECT CHOICE: YOU FALL INTO A PIT OF TARANTULAS. THEY SLOWLY DEVOUR YOU ❌❌❌❌❌❌")
    while True:
        level2_choice = input("\nWould you like to continue with the adventure?: | yes | no |\n").lower().strip()

        if level2_choice == "yes":
            second_floor()
            break

        elif level2_choice == "no":
            slowprint("\nThanks for visiting, come back soon")
            # time.sleep(2)
            game_transition()
            quit()

        elif level2_choice != "yes":
            slowprint("\nIncorrect input, please select yes or no")


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
    # start_game()
    # read_game_intro_files("assets/game-txt-files/game-intro-files/game-rules.txt", "rules")
    # game_transition()
    # read_game_intro_files("assets/game-txt-files/game-intro-files/game-plot.txt", "plot")
    # game_transition()
    # third_floor()
    # game_transition()
    second_floor()

    # validation_checking(answer)


slowprint("\n☠️☠️☠️☠️☠️☠️ WELCOME TO THE EERIE MANSION, CHOOSE YOUR OWN ADVENTURE ☠️☠️☠️☠️☠️☠️\n")
game_main()
