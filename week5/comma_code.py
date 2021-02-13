#!/usr/bin/env python
"""
    Write a program that prints a list with all the items separated by a
    comma and a space, with and inserted before the last item. For example,
    the above list would print 'apples, bananas, tofu, and cats'. But your
    program should be able to work with any list not just the one shown above.
    Because of this, you will need to use a loop in case the list to print
    is shorter or longer than the above list. Make sure your program works
    for all user inputs. For instance, we wouldn't want to print "and" or
    commas if the list only contains one item.
"""

def get_words():
    word_list = []
    while True:
        inp = input(f"Enter a word (leave blank to exit): ").strip()
        if inp == "":
            break  # Terminate on empty line.
        word_list.append(inp)
    return word_list


if __name__ == "__main__":
    print("\nThis program will let you enter a series of words.\n"
          "Once you have entered all of the words press enter to \n"
          "leave the line blank and exit.  At this point a comma-\n"
          "delimited list of words will appear.")
    print(",".join(get_words()))
