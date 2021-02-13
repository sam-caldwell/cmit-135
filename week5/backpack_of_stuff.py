#!/usr/bin/env python
"""
    Backpack of stuff
"""
import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if(userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemsInBackpack.append(input())

    if(userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()
        if itemToCheck in itemsInBackpack:
            print(f"We found {itemToCheck} in the backpack.")

    if(userChoice == "3"):
        sys.exit()