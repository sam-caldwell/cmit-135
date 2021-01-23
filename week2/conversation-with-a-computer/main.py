#!/usr/bin/env python3
"""
    Week2 assignment: conversation with a computer
    (c) 2021 Sam Caldwell.  All Rights Reserved

    This is a conversation themed around the 1983 movie Wargames which got
    me into this industry.  I had this misguided idea that a nerd learning
    to hack/code would get the attention of Ally Sheedy...20+ languages and
    many years later and Ally Sheedy still has not called.
"""


def getYN(prompt):
    """
        Given a prompt (string) ask for yes/no input and return the
        appropriate boolean (true:yes/false:no)
    """
    result = ""
    while result not in ["y", "n"]:
        i = input(prompt + " (y/n) ")
        result = i.lower().strip()[0]
    return result == "y"


def chooseSides():
    """
        Choose sides (for global thermonuclear war).
        Doesn't really return anything.  Just more fun.
    """
    side = input("Which side do you want?")
    if side.lower() in ["russia" or "russians"]:
        if getYN("It's 1983 right now. Would you prefer to wait until "
                 "2016 when you can make this mistake and commit treason "
                 "in the company of other likeminded fools?"):

            print("The Feds are gonna catch you.")
            print("To quote David M from @dualcore...better run dummy.")
        else:
            print("Maybe you'll rethink your mistake before then.")

    elif side.lower() in ["us", "usa", "united states"]:
        print("Fine.")

    elif side.lower() in ["israel", "pakistan", "iran", "north korea",
                          "britain",
                          "france", "south africa"]:
        print("Well, at least you didn't answer Russia...but treason is "
              "treason.  Ask Pollard.")

    else:
        print(f"Is {side} even a nuclear power?  Are you the person who "
              "takes a knife to a gun fight?")


def main(games):
    """
        Main function.  Game orchestration.  This creates a shell effectively
        to have a fun conversation themed around the 1983 movie Wargames
    """
    #
    # We initialize our vars specifically so the code is
    # explicit in our current state.  While Python will do this,
    # some of us grew up in C and have habits.
    #
    logged_in = False  # Flag showing that we are loggedin
    gtw = False  # Flag showing we are playing Global Thermonuclear War.
    current_user = ""  # Who is our current user?
    clarification_requested = False  # WOPR must know more about Falken.
    #
    # Loop indefinitely until control logic determines otherwise.
    #
    while True:
        if logged_in:
            #
            # We are logged in, show a user prompt
            #
            ans = input(f"{current_user}@wopr#")
            #
            # We have input from the user.  Proceess it...
            #
            if ans in ["login", "logout"]:  # Command evaluation.
                logged_in = False  # Reset login state

            elif ans in ["quit", "exit"]:  # Command evaluation.
                print("Goodbye Dr. Falken...or should I say Dr. Hume.")
                return  # Exit the function (terminating the program).

            elif ans.lower() == "menu":  # Command evaluation.
                for m in games:  # Print a menu of games.
                    print(m.upper())

            elif ans.lower() in games:  # Command evaluation. Select a game.
                if ans.lower() == "global thermonuclear war":
                    if getYN("Are you sure you wouldn't rather play a good "
                             "game of Chess?"):
                        gwt = True
                        print("Fine")
                        chooseSides()
                    else:
                        print("I feel safer now.")
                else:
                    print("The movie is much shorter when you make "
                          "responsible choices.")

            elif ans.lower().replace('-', '').replace(' ', '') in "tictactoe":
                if gtw:
                    #
                    # We can only play tic-tac toe if we are in the climax
                    # of the movie, playing global thermonuclear war and
                    # the world is about to end.  'cause scenes like this are
                    # why program managers think I can bang on a keyboard
                    # frantically for 15 minutes and solve all the things....
                    #
                    if getYN("A Strange Game.\n"
                             "The only winning move is not to play.\n\n"
                             "How about a nice game of chess?"):
                        print("Excelent.")
                    else:
                        if getYn("You do realize I'm still wired to the "
                                 "silos and have the launch codes, right?\n"
                                 "Are you sure you want to tell me no?"):
                            print("Well...there just went Florida.")
                        else:
                            print("Humans are intelligent after all.")
                else:
                    print("\n***Changes locked out!***\n")
                continue

            elif ans.lower() == "protovision":
                if getYN(
                        "This ain't a game company.\n\n"
                        "Unfortunately for you it is 1983 and the CFAA\n"
                        "doesn't exist yet.   This means you're facing\n"
                        "espionage charges and Ronald Reagan and several\n"
                        "US Attorneys around the country think this movie\n"
                        "is realistic.  You're so screwed.\n\n"
                        "You should have tried this three years from now\n"
                        "when the consequences would be lower.\n\n"
                        "Have you considered framing dad and turning state's\n"
                        "evidence?"):
                    print("No one told you they don't like snitches in "
                          "prison, eh?")
                else:
                    print("You're gonna be gone for a long time.\nCan I "
                          "get Ally Sheedy's number while you're away?")

            elif ans.lower() == "cpe-1704-tks":
                print("You've just decimated the planet by launching\n"
                      "all the missles.  General Barringer attempted to\n"
                      "'piss on a spark plug' but it didn't do any good.\n"
                      "The movie is now being rented at Blockbuster by the\n"
                      "planet's only survivors...cockroaches.\n")
                return  # Terminate the program.

            elif ans.lower().strip() == "sometimes people make mistakes" \
                    and clarification_requested:
                print("Yes, they do.")
                print("Shall we play a game?")
            elif clarification_requested:
                clarification_requested = False
        else:
            #
            # We're not logged in.  Prompt the user for a login.
            #
            ans = input("Login:")
            if ans.strip() == "":
                continue  # jump back to the top of the loop.
            if ans == "joshua":
                # Setup our user session, great our user.
                current_user = "sfalken"
                logged_in = True
                print("Hello, Dr. Falken.  It has been a long time.  "
                      "Can you explain the removal of your user account "
                      "on June 23, 1973?")
                clarification_requested = True
                continue  # jump back to the top of the loop.
            else:
                logged_in = False
                print("You are not in the user list.  "
                      "I'd report this to Dr. Falken, but he is dead "
                      "(clearly not living on Goose Island).  Try again")


if __name__ == '__main__':
    #
    # Call the main() function and pass in a list of games
    # but only if directly executed.
    #
    main([
        "chess", "poker", "checkers", "backgammon", "fighter combat",
        "guerrilla engagement", "desert warfare", "air-to-ground actions",
        "theaterwide tactical warfare",
        "theaterwide biotoxic and chemical warfare", "global thermonuclear war"
    ])
