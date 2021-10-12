print("Welcome To The Haunted Mansion, Choose Your Own Adventure!")


def start_game():
    """
    Asks the user if they want to play the game,
    depending on thier answer, game starts or exits
    """

    global playing
    playing = input("Would you like to play? (Choose: yes/no): \n")
    if playing.lower().strip() == "yes":
        print("Starting Game")
    elif playing.lower().strip() == "no":
        print("Thanks for visiting, come back soon")
        quit()
