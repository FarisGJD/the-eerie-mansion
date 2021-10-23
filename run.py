"""
The Haunted Mansion
By: Faris Dhoot
"""

# Document Imports
from path import p1_correct_path, p1_correct_path_additions, p1_losing_path, \
    p2_losing_path, p3_game_path, p3_losing_path, losing_p, second_floorp
from functions import handel_game, q_and_a1, q_and_a2, q_and_a3, q_and_a4, \
    q_and_a5, random_number_generator, slowp, game_transition, time

answer = None


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input(
            "Do you dare play? "
            + "Type: | yes | no |\n").lower().strip()

        if playing == "yes":
            slowp("\nInitialising Game")
            time.sleep(2)
            game_transition()
            read_game_intro_files(
                "assets/game-txt-files/game-intro-files/"
                + "game-rules.txt", "rules")
            game_transition()
            read_game_intro_files(
                "assets/game-txt-files/game-intro-files/game-plot.txt", "plot")
            game_transition()
            break

        elif playing == "no":
            slowp("\nThanks for visiting, come back soon")
            quit()

        elif playing != "yes":
            slowp("\nInvalid entery, please select yes or no")


def user_validation():
    """
    Validates User Input
    """
    global answer
    try:
        answer = int(input("Which Door Do You Enter: | 1 | 2 | 3 |\n").strip())
        if answer not in range(1, 4):
            raise ValueError(
                f""" Your answer should either be | 1 | 2 | 3 |
                \ryou entered {answer}"""
            )
    except ValueError:
        print("\nInvalid input, please follow the prompt!\n")

        return user_validation()


def third_floor():
    """"
    Starting game floor
    """
    # Level Introduction
    slowp("""\nThere are three doors in front of you, the first is covered
    \rin cob webs, the second has odd markings engraved on to it and the
    \rthird has a strange liquid seeping through the bottom.\n""")
    user_validation()

    # Main Winning Path (Sequence 1|2|1|2|3|2|2|3|1|2)
    if answer == 1:
        slowp(p1_correct_path['p1'])
        user_validation()

        # Instant Losing Path
        if answer == 1:
            restart3(p1_losing_path['p1'])

        # Continuing Winning Path (2)
        elif answer == 2:
            slowp(p1_correct_path['p2'])
            user_validation()

            # Continuing Winning Path (3)
            if answer == 1:
                slowp(p1_correct_path['p3'])
                read_game_clue_files(
                    "assets/game-txt-files"
                    + "/game-clue-files/novel.txt", "novel")
                slowp(p1_correct_path_additions['p3a'])
                user_validation()

                # Instant Losing Path
                if answer == 1:
                    restart3(p1_losing_path['p2'])

                # Continuing Winning Path (4)
                elif answer == 2:
                    slowp(p1_correct_path['p4'])
                    user_validation()

                    # Instant Losing Path
                    if answer == 1:
                        restart3(p1_losing_path['p3'])

                    # Instant Losing Path
                    elif answer == 2:
                        restart3(p1_losing_path['p4'])

                    # Continuing Winning Path (5)
                    elif answer == 3:
                        slowp(p1_correct_path['p5'])
                        user_validation()

                        # Instant Losing Path
                        if answer == 1:
                            restart3(p1_losing_path['p5'])

                        # Continuing Winning Path (6)
                        elif answer == 2:
                            slowp(p1_correct_path['p6'])
                            user_validation()

                            # Instant Losing Path
                            if answer == 1:
                                restart3(p1_losing_path['p6'])

                            # Continuing Winning Path (7)
                            elif answer == 2:
                                slowp(p1_correct_path['p7'])
                                read_game_clue_files(
                                    "assets/game-txt-files/game-clue-files/"
                                    + "greenhouse-report.txt", "report")
                                slowp(p1_correct_path_additions['p7a'])
                                user_validation()

                                # Instant Losing Path
                                if answer == 1 or answer == 2:
                                    restart3(p1_losing_path['p7'])

                                # Continuing Winning Path (8)
                                elif answer == 3:
                                    slowp(p1_correct_path['p8'])
                                    user_validation()

                                    # Continuing Winning Path (9)
                                    if answer == 1:
                                        slowp(p1_correct_path['p9'])
                                        user_validation()

                                        # Instant Losing Path
                                        if answer == 1:
                                            restart3(p1_losing_path['p8'])

                                        # Continuing Winning Path (10)
                                        elif answer == 2:
                                            slowp(p1_correct_path['p10'])
                                            continue_after_text()
                                            game_transition()

                                        elif answer == 3:
                                            restart3(losing_p["lp"])

                                    # Instant Losing Path
                                    elif answer == 2:
                                        restart3(p1_losing_path['p9'])

                                    elif answer == 3:
                                        restart3(losing_p["lp"])

                            # Game Over Path
                            elif answer == 3:
                                restart3(losing_p["lp"])

                        # Game Over Path
                        elif answer == 3:
                            restart3(losing_p["lp"])

                # Game Over Path
                elif answer == 3:
                    restart3(losing_p["lp"])

            # Instant Losing Path
            elif answer == 2:
                restart3(p1_losing_path['p3ii'])

            # Instant Losing Path
            elif answer == 3:
                slowp(p1_correct_path['p3i'])
                user_validation()

                # Instant Losing Path
                if answer == 1 or answer == 2 or answer == 3:
                    restart3(p1_losing_path['p3i'])

        # Game Over Path
        elif answer == 3:
            restart3(losing_p["lp"])

    # Primary Losing Path
    elif answer == 2:
        restart3(p2_losing_path['p1'])

    # Secondary Losing Path (Sequence | 3 | 2 | 1 | 2 |)
    elif answer == 3:
        slowp(p3_game_path["p1"])
        user_validation()

        if answer == 1:
            restart3(p3_losing_path["p1"])

        elif answer == 2:
            restart3(p3_losing_path["p1i"])

        elif answer == 3:
            slowp(p3_game_path["p2"])
            user_validation()

            if answer == 1:
                restart3(p3_losing_path["p2"])

            elif answer == 2:
                slowp(p3_game_path["p3"])
                user_validation()

                if answer == 1:
                    slowp(p3_game_path["p4"])
                    user_validation()

                    if answer == 1:
                        restart3(p3_losing_path["p3"])

                    elif answer == 2:
                        slowp(p3_game_path["p5"])
                        user_validation()

                        if answer == 1 or answer == 2 or answer == 3:
                            slowp(p3_game_path["p6"])
                            read_game_clue_files(
                                "assets/game-txt-files/game-clue-files/"
                                + "lab-book.txt", "book")
                            restart3(p3_losing_path["p5"])

                elif answer == 2:
                    restart3(p3_losing_path["p4"])

                elif answer == 3:
                    restart3(losing_p["lp"])

            elif answer == 3:
                restart3(losing_p["lp"])


def second_floor():
    """
    Second Game Floor
    """
    slowp("""\nBefore arriving at the end of the stairs you reach a
    \rbalcony. Beneath you is a minesfiled of 3 doors and traps placed
    \rconsecutively. The doors seem to have strange markings on them. You
    \rapproach the first set of 3.\n""")
    user_validation()

    # Winning Path  (Sequence 2 | 1 | 3 | 1 | 3)

    if answer == 1 or answer == 3:
        restart2()

    elif answer == 2:
        slowp("\nYou read the strange markings on the door.")
        handel_game(q_and_a1)
        user_validation()

        if answer == 1:
            slowp("\nYou read the strange markings on the door.")
            handel_game(q_and_a2)
            user_validation()

            if answer == 1 or answer == 2:
                restart2()

            elif answer == 3:
                slowp("\nYou read the strange markings on the door.")
                handel_game(q_and_a3)
                user_validation()

                if answer == 1:
                    slowp("\nYou read the strange markings on the door.")
                    handel_game(q_and_a4)
                    user_validation()

                    if answer == 1 or answer == 2:
                        restart2()

                    elif answer == 3:
                        slowp(
                            "\nYou read the strange markings on the door.")
                        handel_game(q_and_a5)
                        slowp(second_floorp["outro"])
                        continue_after_text()
                        game_transition()

                elif answer == 2 or answer == 3:
                    restart2()

        elif answer == 2 or answer == 3:
            restart2()


def first_floor():
    """
    Function that plays the
    final game floor
    """
    slowp("""\nYou reach the end of the stairs and are enthralled by what
    \ryou see. A giant metallic, cybernated door with two glass screens on
    \reither side. Both have been smeared with some sort of black paint. You
    \ruse your flashlight to scrape off the matter blocking your view, looking
    \rthrough. You being to holler with joy. Behind the glass screen is the
    \rexit from the mansion. Freedom at last.\n
    \rAs you begin to inspect the door, trying to figure out how to operate it
    \ryou notice a computer screen to its side. Upon reading its content you
    \rrealise you need to provide a single integer ranging from 0 – 15 in
    \rorder to exit. Although you are shaking with nerves you begin.\n""")
    random_number_generator()
    time.sleep(2)
    slowp("""\n🥳🥳🥳🥳🥳🥳 YOU’VE DONE IT!!! CONGRATULATIONS. YOU HAVE
    \rSUCCESSFULLY ENTERED THE CORRECT NUMBER. THE COMPUTER TRIGGERS THE
    \rDOOR MECHANISM, OPENING IT. FREEDOM AT LAST. 🥳🥳🥳🥳🥳🥳\n
    \r🏚 Thank you for playing The Eerie Mansion.\n""")
    game_transition()


def restart3(text):
    """
    Takes user back to the begning of
    the third floor
    """
    slowp(f"\n⛔️⛔️⛔️⛔️⛔️ INCORECT PATH: {text} RESTARTING LEVEL ⛔️⛔️⛔️⛔️⛔️")
    while True:
        choice = input(
            "\nWould you like to continue with the adventure?:"
            + " | yes | no |\n").lower().strip()

        if choice == "yes":
            third_floor()
            break

        elif choice == "no":
            slowp("\nThanks for playing, better luck next time.")
            time.sleep(2)
            game_transition()
            quit()

        elif choice != "yes":
            slowp("\nIncorrect input, please select yes or no")


def restart2():
    """
    Takes user back to the begning of
    the second floor
    """
    slowp(
        "\n❌❌❌❌❌❌ INCORECT CHOICE: YOU FALL INTO A PIT OF TARANTULAS."
        + " ❌❌❌❌❌❌")

    while True:
        choice = input(
            "\nWould you like to continue with the adventure?:"
            + " | yes | no |\n").lower().strip()

        if choice == "yes":
            second_floor()
            break

        elif choice == "no":
            slowp("\nThanks for the fun, come back prepared")
            time.sleep(2)
            game_transition()
            quit()

        elif choice != "yes":
            slowp("\nIncorrect input, please select yes or no")


def read_game_intro_files(intro_file, text):
    """
    Reads game introductory files
    """
    while True:
        rules_file_answer = input(
            f"\nWould you like to read the {text}?"
            + " Choose: | yes | no |\n").lower().strip()

        if rules_file_answer == "yes":
            with open(intro_file) as file:
                choice_text = file.read()
                slowp(choice_text)
                continue_after_text()
                break

        elif rules_file_answer == "no":
            break

        elif rules_file_answer != "yes":
            slowp("\nInvalid entery, please select yes or no")


def read_game_clue_files(clue_file, text):
    """
    Reads the games clues and path choice
    files
    """
    while True:
        clues = input(
            f"Would you like to read the {text}?"
            + " Choose: | yes | no |\n").lower().strip()

        if clues == "yes":
            with open(clue_file) as file:
                text = file.read()
                slowp(text)
                continue_after_text()
                break

        elif clues == "no":
            break

        elif clues != "yes":
            slowp("\nInvalid entery, please select yes or no")


def continue_after_text():
    """
    Allows user time to read game files
    then gives them the option to continue
    """
    while True:
        progress = input(
            "\nClick 'c' and enter on your kerboard"
            + " to continue\n").lower().strip()

        if progress == "c":
            break

        elif progress != "c":
            print("Invalid entery, please select the 'c' key")


def game_main():
    """
    Implements the games principle functions
    """
    start_game()
    third_floor()
    second_floor()
    first_floor()


slowp("""\n☠️☠️☠️☠️☠️☠️ WELCOME TO THE EERIE MANSION, CHOOSE YOUR OWN \
ADVENTURE ☠️☠️☠️☠️☠️☠️\n""")
game_main()
