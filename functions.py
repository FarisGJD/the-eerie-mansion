"""
Functions For
Level 2
& Level 3
"""

import random
import sys
import time

# Level 2 Questions Game


class Question(object):
    """
    Stores Questions Cue
    & Answers
    """
    def __init__(self, cue, answers):
        self.cue = cue
        self.answers = answers


questions_cues = [
    """\nWhat is the name of the killer clown in Stephen Kings IT?
    \n(a) BOZO
    \n(b) Captain Spaulding
    \n(c) Pennywise
    \n(d) Mr Mime\n\n""",

    """\nWhat is the name of the main villian in the origional Texas Chainsaw
    \rMassacre?
    \n(a) Leatherface
    \n(b) Pinhead
    \n(c) Ghostface
    \n(d) Slicey Mcstabby\n\n""",

    """\nWhat is the name of the hotel where "The Shinning" Takes Place
    \n(a) The Grand Frontier
    \n(b) Overwatch Hotel
    \n(c) Glacier Peak
    \n(d) The Stanley Hotel\n\n""",

    """\nWhat was the name of the fishing boat used at the end of "JAWS"?
    \n(a) Spellbound
    \n(b) Orca
    \n(c) High Tide
    \n(d) Buoy O Buoy\n\n""",

    """\nHow dose the unseen monster from 'It Follows' decide who to target?
    \n(a) Sexual Partner
    \n(b) Virgins
    \n(c) Atheists
    \n(d) Females Only\n\n"""
]

q_and_a1 = [
    Question(questions_cues[0], "c")
]

q_and_a2 = [
    Question(questions_cues[1], "a")
]

q_and_a3 = [
    Question(questions_cues[2], "d")
]

q_and_a4 = [
    Question(questions_cues[3], "b")
]

q_and_a5 = [
    Question(questions_cues[4], "a")
]


def handel_game(questions):
    """
    Asks User Questions,
    Checks if they are right,
    decreases score if wrong.
    """
    for que in questions:
        user_answer = input(que.cue).lower().strip()
        if user_answer == que.answers:
            slowp("\nCorrect!!!\n")
        else:
            slowp("\nIncorrect answer\n")


# Level 1 Random Number Guessing Game

def random_number_generator():
    """
    Generates Random Number
    For First Floor
    """
    random_num = random.randint(0, 15)
    score = 5

    while True:
        guess = input("The computer needs a number between 0 - 15\n")
        if guess.isdigit():
            guess = int(guess)

        else:
            slowp("\nIncorrect input please follow the prompt\n")
            continue

        if guess == random_num:
            slowp("\nCorrect!!!\n")
            break

        elif guess != random_num:
            score -= 1
            slowp(f"\nYou have {score} lives remaining")

            if guess > random_num:
                slowp("\nGuess too high, try a lower integer.")

            elif guess < random_num:
                slowp("\nGuess too low, try a higher integer.\n")

                if score == 0:
                    game_over("""YOU ARE OUT OF LIVES, THE COMPUTER EXPLODES,
                    \rLOCKING THE DOOR FOREVER TRAPPING YOU INSIDE.""")


def slowp(slow):
    """
    Function that uses the sys & time modules to
    print text slow in the terminal
    """
    for slw in slow + '\n':
        sys.stdout.write(slw)
        sys.stdout.flush()
        time.sleep(0.25/10)


def game_transition():
    """
    Adds a "tranisitional" effect to the game within
    the terminal (strictly visual)
    """
    slowp("""\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.
    \r\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.""")


def game_over(text):
    """
    Informs the user that they have lost the game,
    restarting the programme.
    """
    slowp(f"\n🕷🕷🕷🕷🕷🕷 {text} GAME OVER 🕷🕷🕷🕷🕷🕷")
    game_transition()
    slowp("""\nThanks for playing, please come again.\n""")
    exit()
