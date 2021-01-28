#!/usr/bin/env python3
"""
    Week3 assignment, task 4
    (c) 2021 Sam Caldwell.  All Rights Reserved

    With messaging in honor of Samuel L. Jackson
"""
from random import randint

correct = [
    "That is correct.",
    "Bingo!",
    "Winner, Winner.  Chicken Dinner!",
    "Your momma would be proud.",
    "Even a chump like you get's lucky once or twice.",
    "Would you look at that.",
    "Damn!  Not bad.",
    "You are a demonstration in the law of averages.  Or just average.",
    "Bet you think you're smart now, don't ya?",
    "Oh!  Look who thinks he won the lottery.",
]

incorrect = [
    "Nope",
    "Missed it",
    "Not even close",
    "Keep trying",
    "Well, you definitely are not clarvoyant",
    "No.  Give up yet?",
    "Are you even trying?",
    "Which part of 'no' do you not understand?",
    "At least you're persistent...but NO!",
    "Hell, no."
]

inp = ""
while inp.lower() != "q":
    # Cast to string to eliminate error handling.
    # Less expensive than a try...except.
    randomNum = f"{randint(0,9)}"
    inp = input("Guess a number (0-9): ")
    if inp == randomNum:
        msg = randint(0,len(correct)-1)
        print(f"\tResponse: [correct]: {correct[msg]}")
    elif inp.lower() != "q":
        msg = randint(0,len(incorrect)-1)
        print(f"\tResponse: [incorrect]: {incorrect[msg]}")
print("I ain't sad to see you go.")