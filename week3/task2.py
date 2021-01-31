#!/usr/bin/env python3
"""
    Week3 assignment, task 2
    (c) 2021 Sam Caldwell.  All Rights Reserved

    (With added messages quoting things my dad might (did) say.)
"""
scale = {"F": 60,
         "D-": 63,
         "D": 67,
         "D+": 70,
         "C-": 73,
         "C": 77,
         "C+": 80,
         "B-": 83,
         "B": 87,
         "B+": 90,
         "A-": 93}

msg = {
    "F":"Boy, F is for failure. Do you like pumping gas?  "
        "--Sam Caldwell, Sr.",
    "D-": "A 'D-'? What happened? Couldn't get a solid D?  "
          "--Sam Caldwell, Sr.",
    "D": "A 'D'.  You Drilling for oil with this grade?  "
         "--Sam Caldwell, Sr.",
    "D+": "D+ is still a d, boy.  --Sam Caldwell, Sr.",
    "C-": "Couldn't get a real C?  --Sam Caldwell, Sr.",
    "C": "C may be passing at A&M but not here.  "
         "--Sam Caldwell, Sr.",
    "C+": "Try harder, boy.  --Sam Caldwell, Sr.",
    "B-": "Well, I could always send you to A&M. "
          "-- Sam Caldwell,Sr.",
    "B": "Boy, I know you tried hard.  "
         "But trying doesn't count.   "
         "--Sam Caldwell, Sr.",
    "B+": "You got this from your mother's side.  "
          "--Sam Caldwell, Sr.",
    "A-": "Almost counts in horseshoes and hand grenades.  "
          "Was this class in either of those subjects?  "
          "--Sam Caldwell, Sr.",
    "A": "You only got one A on this assignment? --Sam Caldwell Sr."
}
inp = ""
while inp.lower() != "q":
    try:
        inp = input("Enter your grade (0-100 or q to quit): ")
        grade = int(inp)
        if grade < 0:
            print("Invalid grade.  Number must be 0-100.")
            continue
        elif grade > 100:
            print("Invalid grade.  Number must be 0-100.\n\n"
                  "\tEither those teachers are coddling you with extra\n"
                  "\tcredit or you have clearly been forging your grades\n"
                  "\tagain.\n")
            continue
        letter_grade = "A"
        for letter, number in scale.items():
            if grade < number:
                letter_grade = letter
                break
        print(f"{letter_grade}\n\n\t{msg[letter_grade]}\n")
    except ValueError:
        print("You must enter a number for your grade (0-100).")
        grade = -1
print("Terminating")