#!/usr/bin/env python3
"""
    Week3 assignment, task 1
    (c) 2021 Sam Caldwell.  All Rights Reserved
"""


age=-1
while age < 18:
    try:
        age=int(input("Enter your age: "))
        if age < 18:
            print("You must be 18 to vote.")
        else:
            print("You are of voting age.")
    except ValueError:
        print("You must enter a number for your age.")