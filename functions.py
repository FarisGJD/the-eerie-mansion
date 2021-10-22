"""
Functions For
Level 2
& Level 3
"""

import random

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
    score = 5
    for que in questions:
        user_answer = input(que.cue)
        if user_answer == que.answers:
            print("\nCorrect!!!\n")
        else:
            score -= 1
            print(f"\nIncorrect answer, you have {score} lives left\n")


# Level 1 Random Number Guessing Game

def random_number_generator():
    """
    Generates Random Number
    For First Floor
    """
    random_num = random.randint(0, 10)
    score = 5

    while True:
        guess = input("The computer needs a numbe between 0 - 10\n")
        if guess.isdigit():
            guess = int(guess)

        else:
            print("Input number")
            continue

        if guess == random_num:
            print("Correct")
            break

        elif guess > random_num:
            print("above")

        elif guess < random_num:
            print("below")

        elif guess != random_num:
            score -= 1
            print(f"You have {score} remaining")
            if score == 0:
                quit()


random_number_generator()
