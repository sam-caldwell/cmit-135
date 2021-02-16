"""
    DO NOT USE THIS AS A PASSWORD MANAGER.  THIS IS NOT A SECURE
    SOLUTION.  THIS IS FOR A CLASS AND IS USED TO TEACH PYTHON
    ONLY.
"""
from os.path import exists
from string import ascii_letters, digits, punctuation
import json
import sys

password_file_name = "defaultPasswordFile.json"

encryption_key = 0

key_space = (ascii_letters + digits + punctuation).split()

MENU_SET_KEY = 1
MENU_SET_FILE = 2
MENU_OPEN_FILE = 3
MENU_SEARCH = 4
MENU_ADD = 5
MENU_DELETE = 6
MENU_SAVE = 7
MENU_DUMP = 8
MENU_QUIT = 9

menu = {
    f"{MENU_SET_KEY}": "Set encryption key",
    f"{MENU_SET_FILE}": "Set password file",
    f"{MENU_OPEN_FILE}": "Open password file",
    f"{MENU_SEARCH}": "Lookup a password",
    f"{MENU_ADD}": "Add a password",
    f"{MENU_DELETE}": "Delete password",
    f"{MENU_SAVE}": "Save password file",
    f"{MENU_DUMP}": "Print the encrypted password list (for testing)",
    f"{MENU_QUIT}": "Quit program"
}

passwords = {}


def invert_key(key):
    return -1 * int(key)


def clear_screen():
    # ToDo: clear screen for better UI (ncurses maybe)
    pass


def get_option(prompt, choices):
    while True:
        try:
            return int(input(f"{prompt} ({choices[0]}-{choices[-1]}): "))
        except ValueError:
            print("Invalid choice.  Try again.")


def print_menu():
    clear_screen()
    print("What would you like to do:")
    for k, v in menu.items():
        print(f"   {k}. {v}")
    return get_option("Please enter a number", [1, len(menu)])


def load_password_file(password_file_name):
    if exists(password_file_name):
        with open(password_file_name, 'r') as fileHandle:
            print(f"Open and read file: {password_file_name}")
            return json.loads(fileHandle.read())
            print(f"Loaded {len(passwords)} Records")
    else:
        with open(file_name, 'w') as fileHandle:
            print(f"Creating new file (file not found): {password_file_name}")
            fileHandle.write(json.dumps({}, indent=4))
            return {}


def save_password_file():
    print("Save Passwords")
    with open(password_file_name, 'w+') as fileHandle:
        fileHandle.write(json.dumps(passwords, indent=4))


def dump_passwords():
    print("Print out the password list")
    print("-" * 40)
    n = 0
    for key, value in passwords.items():
        print(f"{n:3} {key:20} : {value}")
        n += 1
    print("-" * 40)
    print(f"Count: {len(passwords)}")
    print("-" * 40)


def add_password():
    print("Password Lookup")
    site = input("What is this password for? ")
    passwords[site] = caeser_cipher(
        input("Enter the password: "),
        encryption_key)
    print(f"Password added for {site}")


def delete_password():
    print("Delete Password")
    query = input("Which website are you searching for? ")
    print(f"Deleting password for {query}")
    if query in passwords:
        passwords.pop(query)
        save_password_file()
    else:
        print(f"{query} not found.")


def password_lookup():
    query = input("Which website are you searching for? ")
    if query in passwords:
        print(caeser_cipher(passwords[query], invert_key(encryption_key)))
    else:
        print(f"Record not found for {query} : {password}")


def caeser_cipher(plain_text, key):
    # Caesar Cipher Encryption
    # We will start with an empty string as our cipher_text
    cipher_text = ''

    # For each symbol in the unencryptedMessage we will
    # add an encrypted symbol into the cipher_text

    # ToDo: Fix the cipher algorithm to handle the entire keyspace.

    for symbol in plain_text:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            cipher_text += chr(num)
        else:
            cipher_text += symbol
    return cipher_text


def set_encryption_key():
    min = 0
    max = len(key_space) + 1
    while True:
        try:
            return int(input("Set encryption key: "))
        except ValueError:
            print(f"Invalid encryption key.  Key must be ({min}...{max})")
            continue


def set_password_file_name():
    while True:
        fn = input("Enter the name of the password file: ")
        if exists(fn):
            print("This file already exists.  You cannot use this name.")
        else:
            return fn


while True:
    choice = print_menu()
    if choice == MENU_SET_KEY:
        encryption_key = set_encryption_key()
    elif choice == MENU_SET_FILE:
        password_file_name = set_password_file_name()
    elif choice == MENU_OPEN_FILE:
        passwords = load_password_file(password_file_name)
    elif choice == MENU_SEARCH:
        password_lookup()
    elif choice == MENU_ADD:
        add_password()
    elif choice == MENU_DELETE:
        delete_password()
    elif choice == MENU_SAVE:
        save_password_file()
    elif choice == MENU_DUMP:
        dump_passwords()
    elif choice == MENU_QUIT:
        print("Terminating.")
        sys.exit(0)
    else:
        print("Internal Error: Unknown or unrecognized option.")
    print("\n")
