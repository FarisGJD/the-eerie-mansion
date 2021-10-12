print("Welcome To The Haunted Mansion, Choose Your Own Adventure!")

playing = input("Would you like to play (Choose: yes/no):\n ")


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """
    if playing.lower().strip() == "yes":
        print("Starting Game")
    elif playing.lower().strip() == "no":
        print("Thanks for visiting, come back soon")
        quit()


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


def game_main():
    """
    Implements the games principle functions
    """
    start_game()
    validation_checking(playing)


game_main()
