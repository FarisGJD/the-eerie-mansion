# Document imports

import time

print("Welcome To The Haunted Mansion, Choose Your Own Adventure!")


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    while True:
        playing = input("Would you like to play (yes/no):\n ").lower().strip()

        if playing == "yes":
            print("Initialising Game...")
            time.sleep(2)
            game_transition()
            break

        elif playing == "no":
            print("Thanks for visiting, come back soon")
            quit()

        elif playing != "yes":
            print("Invalid entery, please select yes or no")


def validation_checking(playing_answer):
    """
    Checks for errors made by user input and throws
    relevant warning
    """
    try:
        if playing_answer != "yes":
            raise ValueError(
                (f"""Your answer should either be yes or no,
                 you entered {playing_answer}""")
            )

    except ValueError as error:
        print(f"Invalid input: {error}, please try again. \n")


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    print(""".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")
    


def game_main():
    """
    Implements the games principle functions
    """
    start_game()


game_main()
