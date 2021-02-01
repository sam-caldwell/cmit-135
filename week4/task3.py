#!/usr/bin/env python3
"""
    Week4 assignment, task 3
    (c) 2021 Sam Caldwell.  All Rights Reserved
"""
from random import randint

min = 1
max = 100

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

inp = ""
while inp.lower() != "q":
    try:
        # Cast to string to eliminate error handling.
        # Less expensive than a try...except.
        randomNum = f"{randint(min,max)}"
        inp = input(f"Guess a number ({min}-{max}): ")
        if inp == randomNum:
            msg = randint(0,len(correct)-1)
            print(f"\tResponse: [correct]: {correct[msg]}")
        elif inp.lower() == "q":
            print("Terminating")
            break
        elif int(inp) < int(randomNum):
            print(f"\tResponse: [incorrect]: too low")
        elif int(inp) > int(randomNum):
            print(f"\tResponse: [incorrect]: too high")
    except ValueError:
        print("You did not enter a number.")

print("I ain't sad to see you go.")