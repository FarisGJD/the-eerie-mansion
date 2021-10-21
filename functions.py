"""
Functions For
Level 2
& Level 3
"""

# Level 2 Questions


class Question:
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

questions_and_answers1 = [
    Question(questions_cues[0], "c")
]

questions_and_answers2 = [
    Question(questions_cues[1], "a")
]

questions_and_answers3 = [
    Question(questions_cues[2], "d")
]

questions_and_answers4 = [
    Question(questions_cues[3], "b")
]

questions_and_answers5 = [
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
            print("\nCorrect! You Successfully Pass Through")

        elif user_answer != que.answers:
            score -= 1
            print(f"Inncorect Answer Your Life Points Is:{score}")
