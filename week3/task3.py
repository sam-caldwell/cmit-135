#!/usr/bin/env python3
"""
    Week3 assignment, task 3
    (c) 2021 Sam Caldwell.  All Rights Reserved
"""
def enter_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            #
            # Error handling by R. Lee Ermey...
            # ...which is still friendlier than a JAVA stacktrace.
            #
            print("""
                R. Lee Error says...
                
                What is your major malfunction?  I asked for a NUMBER!
                
                Was THIS what you would call a number?!  Do you know how to 
                count?  Did your momma send you to Berkley and call you 
                special so that you would come here and create your own 
                numbering system?  
                
                I don't think so!
                
                Let's try this again!
                """)

numA = enter_number()
numB = enter_number()

if numA + numB > 100:
    print("They add up to a big number")
else:
    print(f"They add up to {numA+numB}")
