"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
import sys
import time
from path import p1_correct_path, p1_correct_path_additions, p1_losing_path, \
    p2_losing_path, p3_game_path, p3_losing_path, game_over_p
from functions import handel_game, q_and_a1, q_and_a2, q_and_a3, q_and_a4, \
    q_and_a5


def slow_print(slow):
    """
    Function that uses the sys & time modules to
    print text slow in the terminal
    """
    for slw in slow + '\n':
        sys.stdout.write(slw)
        sys.stdout.flush()
        time.sleep(0.00000000000000003/10)


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input("Do you dare play? Type: | yes | no |\n").lower().strip() # noqa

        if playing == "yes":
            slow_print("\nInitialising Game")
            # time.sleep(2)
            game_transition()
            read_game_intro_files( \
                "assets/game-txt-files/game-intro-files/game-rules.txt", "rules") # noqa
            game_transition()
            read_game_intro_files( \
                "assets/game-txt-files/game-intro-files/game-plot.txt", "plot") # noqa
            game_transition()
            break

        elif playing == "no":
            slow_print("\nThanks for visiting, come back soon")
            quit()

        elif playing != "yes":
            slow_print("\nInvalid entery, please select yes or no")


def user_validation(text):
    """
    Validates User Input
    """
    global answer
    try:
        answer = int(input(f"{text}\n").strip())
        if answer not in range(1, 4):
            raise ValueError(
                f""" Your answer should either be,
                you entered {answer}"""
            )
    except ValueError:
        print("\nInvalid input, please follow the prompt\n")

        return user_validation(text), answer


def third_floor():
    """"
    Starting game floor
    """
    # Level Introduction
    slow_print("""\nThere are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.\n""")
    user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

    # Main Winning Path (Sequence 1|2|1|2|3|2|2|3|1|2)
    if answer == 1:
        slow_print(p1_correct_path['p1'])
        user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

        # Instant Losing Path
        if answer == 1:
            level_restart3(p1_losing_path['p1'])

        # Continuing Winning Path (2)
        elif answer == 2:
            slow_print(p1_correct_path['p2'])
            user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

            # Continuing Winning Path (3)
            if answer == 1:
                slow_print(p1_correct_path['p3'])
                read_game_clue_files(
                    "assets/game-txt-files"
                    + "/game-clue-files/novel.txt", "novel")
                slow_print(p1_correct_path_additions['p3a'])
                user_validation("\nWhich Door Do You Enter: | 1 | 2 | 3 |")

                # Instant Losing Path
                if answer == 1:
                    level_restart3(p1_losing_path['p2'])

                # Continuing Winning Path (4)
                elif answer == 2:
                    slow_print(p1_correct_path['p4'])
                    user_validation("Which Door Do You Enter:| 1 | 2 | 3 |")

                    # Instant Losing Path
                    if answer == 1:
                        level_restart3(p1_losing_path['p3'])

                    # Instant Losing Path
                    elif answer == 2:
                        level_restart3(p1_losing_path['p4'])

                    # Continuing Winning Path (5)
                    elif answer == 3:
                        slow_print(p1_correct_path['p5'])
                        user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

                        # Instant Losing Path
                        if answer == 1:
                            level_restart3(p1_losing_path['p5'])

                        # Continuing Winning Path (6)
                        elif answer == 2:
                            slow_print(p1_correct_path['p6'])
                            user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

                            # Instant Losing Path
                            if answer == 1:
                                level_restart3(p1_losing_path['p6'])

                            # Continuing Winning Path (7)
                            elif answer == 2:
                                slow_print(p1_correct_path['p7'])
                                read_game_clue_files( \
                                    "assets/game-txt-files/game-clue-files/greenhouse-report.txt", "report") # noqa
                                slow_print(p1_correct_path_additions['p7a'])
                                user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

                                # Instant Losing Path
                                if answer == 1 or answer == 2:
                                    level_restart3(p1_losing_path['p7'])

                                # Continuing Winning Path (8)
                                elif answer == 3:
                                    slow_print(p1_correct_path['p8'])
                                    user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

                                    # Continuing Winning Path (9)
                                    if answer == 1:
                                        slow_print(p1_correct_path['p9'])
                                        user_validation("Which Door Do You Enter: | 1 | 2 |")

                                        # Instant Losing Path
                                        if answer == 1:
                                            level_restart3(p1_losing_path['p8']) # noqa

                                        # Continuing Winning Path (10)
                                        elif answer == 2:
                                            slow_print(p1_correct_path['p10']) # noqa
                                            continue_after_text()
                                            game_transition()

                                        elif answer == 3:
                                            game_over(game_over_p["go"])

                                    # Instant Losing Path
                                    elif answer == 2:
                                        level_restart3(p1_losing_path['p9']) # noqa

                                    elif answer == 3:
                                        game_over(game_over_p["go"])

                            # Game Over Path
                            elif answer == 3:
                                game_over(game_over_p["go"])             

                        # Game Over Path
                        elif answer == 3:
                            game_over(game_over_p["go"])

                # Game Over Path
                elif answer == 3:
                    game_over(game_over_p["go"])

            # Instant Losing Path
            elif answer == 2:
                level_restart3(p1_losing_path['p3ii'])

            # Instant Losing Path
            elif answer == 3:
                slow_print(p1_correct_path['p3i'])
                user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

                # Instant Losing Path
                if answer == 1 or answer == 2 or answer == 3:
                    level_restart3(p1_losing_path['p3i'])

        # Game Over Path
        elif answer == 3:
            game_over(game_over_p["go"])

    # Primary Losing Path
    elif answer == 2:
        level_restart3(p2_losing_path['p1'])

    # Secondary Losing Path (Sequence | 3 | 2 | 1 | 2 |)
    elif answer == 3:
        slow_print(p3_game_path["p1"])
        user_validation("Which Door Do You Enter: | 1 | 2 | 3 |")

        if answer == 1:
            level_restart3(p3_losing_path["p1"])

        elif answer == 2:
            level_restart3(p3_losing_path["p1i"])

        elif answer == 3:
            slow_print(p3_game_path["p2"])
            user_validation("Which Door Do You Enter: | 1 | 2 |")

            if answer == 1:
                level_restart3(p3_losing_path["p2"])

            elif answer == 2:
                slow_print(p3_game_path["p3"])
                user_validation("Which Door Do You Enter: | 1 | 2 |")

                if answer == 1:
                    slow_print(p3_game_path["p4"])
                    user_validation("Which Door Do You Enter: | 1 | 2 |")

                    if answer == 1:
                        level_restart3(p3_losing_path["p3"])

                    elif answer == 2:
                        slow_print(p3_game_path["p5"])
                        user_validation("Which Door Do You Enter: | 1 | 2 | 3 |\n")

                        if answer == 1 or answer == 2 or answer == 3:
                            slow_print(p3_game_path["p6"])
                            read_game_clue_files("assets/game-txt-files/game-clue-files/lab-book.txt", "book") # noqa
                            level_restart3(p3_losing_path["p5"])

                elif answer == 2:
                    level_restart3(p3_losing_path["p4"])


def second_floor():
    """
    Second Game Floor
    """
    slow_print("""\nBefore arriving at the end of the stairs you reach a
    \rbalcony. Beneath you is a mind filed of 3 doors and traps placed
    \rconsecutively. The doors seem to have strange markings on them. You
    \rapproach the first set of 3.\n""")
    answer2 = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip()) # noqa

    # Winning Path  (Sequence 2 | 1 | 3 | 1 | 3)

    if answer2 == 1 or answer2 == 3:
        level_restart2()

    elif answer2 == 2:
        slow_print("\nYou read the strange markings on the door.")
        handel_game(q_and_a1)
        answer2 = int(input("\nWhich Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip()) # noqa

        if answer2 == 1:
            slow_print("\nYou read the strange markings on the door.")
            handel_game(q_and_a2)
            answer2 = int(input( \
                "\nWhich Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip()) # noqa

            if answer2 == 1 or answer2 == 2:
                level_restart2()

            elif answer2 == 3:
                slow_print("\nYou read the strange markings on the door.")
                handel_game(q_and_a3)
                answer2 = int(input( \
                    "\nWhich Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip()) # noqa

                if answer2 == 1:
                    slow_print("\nYou read the strange markings on the door.")
                    handel_game(q_and_a4)
                    answer2 = int(input( \
                        "\nWhich Door Do You Enter: | 1 | 2 | 3 |\n").lower().strip()) # noqa

                    if answer2 == 1 or answer2 == 2:
                        level_restart2()

                    elif answer2 == 3:
                        slow_print("\nYou read the strange markings on the door.") # noqa
                        handel_game(q_and_a5)
                        slow_print("DONT FORGET TO WRITE A STORY TRANISITON HERE") # noqa
                        game_transition()

                elif answer2 == 2 or answer2 == 3:
                    level_restart2()

        elif answer2 == 2 or answer2 == 3:
            level_restart2()


def first_floor():
    """
    Function that plays the
    final game floor
    """


def level_restart3(text):
    """
    Takes user back to the begning of
    the third floor
    """
    slow_print(f"\n⛔️⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} RESTARTING LEVEL ⛔️⛔️⛔️⛔️⛔️⛔️") # noqa
    while True:
        level3_choice = input("\nWould you like to continue with the adventure?: | yes | no |\n").lower().strip() # noqa

        if level3_choice == "yes":
            third_floor()
            break

        elif level3_choice == "no":
            slow_print("\nThanks for visiting, come back soon")
            # time.sleep(2)
            game_transition()
            quit()

        elif level3_choice != "yes":
            slow_print("\nIncorrect input, please select yes or no")


def level_restart2():
    """
    Takes user back to the begning of
    the second floor
    """
    slow_print("\n❌❌❌❌❌❌ INCORECT CHOICE: YOU FALL INTO A PIT OF TARANTULAS. THEY SLOWLY DEVOUR YOU ❌❌❌❌❌❌") # noqa
    while True:
        level2_choice = input( "\nWould you like to continue with the adventure?: | yes | no |\n").lower().strip() # noqa

        if level2_choice == "yes":
            second_floor()
            break

        elif level2_choice == "no":
            slow_print("\nThanks for visiting, come back soon")
            # time.sleep(2)
            game_transition()
            quit()

        elif level2_choice != "yes":
            slow_print("\nIncorrect input, please select yes or no")


def game_over(text):
    """
    Informs the user that they have lost the game,
    restarting the programme.
    """
    slow_print(f"\n☠️☠️☠️☠️☠️☠️{text} GAME OVER☠️☠️☠️☠️☠️☠️")
    game_transition()
    slow_print("""\nThanks for playing, next time  keep the game over paths in
    \rmind.\n""")

    exit()


def read_game_intro_files(intro_file, text):
    """
    Reads game introductory files
    """
    while True:
        rules_file_answer = input( \
            f"\nWould you like to read the {text}? Choose: | yes | no |\n").lower().strip() # noqa

        if rules_file_answer == "yes":
            with open(intro_file) as file:
                choice_text = file.read()
                slow_print(choice_text)
                continue_after_text()
                break

        elif rules_file_answer == "no":
            break

        elif rules_file_answer != "yes":
            slow_print("\nInvalid entery, please select yes or no")


def read_game_clue_files(clue_file, text):
    """
    Reads the games clues and path choice
    files
    """
    while True:
        clues = input( \
            f"Would you like to read the {text}? Choose: | yes | no |\n").lower().strip() # noqa

        if clues == "yes":
            with open(clue_file) as file:
                text = file.read()
                slow_print(text)
                continue_after_text()
                break

        elif clues == "no":
            break

        elif clues != "yes":
            slow_print("\nInvalid entery, please select yes or no")


def continue_after_text():
    """
    Allows user time to read game files
    then gives them the option to continue
    """
    while True:
        progress = input(\
            "\nClick 'c' and enter on your kerboard to continue\n").lower().strip() # noqa

        if progress == "c":
            break

        elif progress != "c":
            print("Invalid entery, please select the 'c' key")


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    slow_print("""\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.
    \r\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")


def game_main():
    """
    Implements the games principle functions
    """
    # start_game()
    third_floor()
    # second_floor()

slow_print("\n☠️☠️☠️☠️☠️☠️ WELCOME TO THE EERIE MANSION, CHOOSE YOUR OWN ADVENTURE ☠️☠️☠️☠️☠️☠️\n") # noqa
game_main()
