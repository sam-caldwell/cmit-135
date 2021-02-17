import sys
import json
from typing import Optional
from os.path import exists
from random import randint
from string import ascii_letters, digits, punctuation

MENU_SET_KEY = 1
MENU_SET_FILE = 2
MENU_OPEN_FILE = 3
MENU_SEARCH = 4
MENU_ADD = 5
MENU_DELETE = 6
MENU_SAVE = 7
MENU_DUMP = 8
MENU_QUIT = 9


class Cache(object):
    """
        This is a simple in-memory cache based on a dict with a getter
        and setter.
    """

    __store = {}  # Internal state.

    def __init__(self):
        """
            Class constructor.  Guarantee internal state.
        """
        self.reset()

    def __del__(self):
        """
            Class destructor.  Noop.
        """
        pass

    def count(self) -> int:
        """
            Return current cache counter (number records)
        """
        return len(self.__store)

    def reset(self):
        """
            Reset the cache to empty state.
        """
        self.__store = {}

    def set(self, key: str, value: str):
        """
            Create/Update a record in the cache.
        """
        self.__store[key] = value

    def get(self, key: str) -> Optional[str]:
        """
            Return an existing cache record or None (if non existent).
        """
        return self.__store[key]

    def delete(self, key: str) -> bool:
        """
            Delete a record identified by a given key and return True
            or return False
        """
        try:
            self.__store.pop(key)
            return True
        except KeyError:
            return False

    def exists(self, key: str) -> bool:
        """
            return true/false if key exists in cache
        """
        return key in self.__store

    def dump(self) -> dict:
        """
            Serialize the dict as a JSON string and return the result
            with intended formatting.
        """
        return json.dumps(self.__store, indent=4)

    def pretty_print(self):
        """
            Print a pretty report of the records in the cache.
        """
        print("-" * 40)
        n = 0
        for key, value in self.__store.items():
            print(f"{n:3} {key:20} : {value}")
            n += 1
        print("-" * 40)
        print(f"Count: {self.count()}")
        print("-" * 40)

    def load(self, serialized_json: str):
        """
            Deserialize a JSON string input and store as the current cache.
        """
        try:
            self.__store = json.loads(serialized_json)
        except Exception:
            print("Error: Failed to deserialize JSON.  File is corrupt.")


class Storage(object):
    """
        File handling (CRUD) operations with in-memeory caching
    """
    cache = Cache()
    password_file = ""

    def __init__(self):
        """
            Class constructor
        """
        self.password_file = "defaultPasswordFile.json"

    def get_file_name(self) -> str:
        """
            return file name.
        """
        return self.password_file

    def set_file_name(self):
        """
            Set a new password file name.
        """
        self.password_file = input("Enter the name of the password file: ")
        print(f"New File set: {self.password_file}")

    def save(self):
        """
            Write the in-memory cache (dict) as a JSON object to disk.
        """
        print("Save Passwords")
        with open(self.password_file, 'w+') as fileHandle:
            fileHandle.write(self.cache.dump())

    def load(self):
        """
            Load the password file containing a JSON object into the
            global in-memory cache (dict).  If the file does not exist
            create the file with an empty {} json/dict object.
        """
        if exists(self.password_file):
            with open(self.password_file, 'r') as fileHandle:
                print(f"Open and read file: {self.password_file}")
                self.cache.load(fileHandle.read())
                print(f"Load {self.cache.count()} Records")
        else:
            print(f"Create new file (file not found): {self.password_file}")
            self.cache.reset()
            self.save()


class Menu(Storage):
    """
        UI class for menu display/interaction.
    """

    def get_option(self, prompt: str, choices: list) -> int:
        """
            Get a numeric option, perform a bounds-check to ensure the number
            is in range of our menu options and return this integer.
        """
        while True:
            try:
                return int(input(f"{prompt} ({choices[0]}-{choices[-1]}): "))
            except ValueError:
                print("Invalid choice.  Try again.")

    def print_menu(self) -> int:
        """
            Print our menu to screen using the global menu list.
            Then prompt the user to select an item from the menu
            and return the numeric selection (integer)
        """
        print("What would you like to do:")
        menu = {
            f"{MENU_SET_KEY}": "Set encryption key",
            f"{MENU_SET_FILE}": "Set password file",
            f"{MENU_OPEN_FILE}": f"Open password file ({self.password_file})",
            f"{MENU_SEARCH}": "Lookup a password",
            f"{MENU_ADD}": "Add a password",
            f"{MENU_DELETE}": "Delete password",
            f"{MENU_SAVE}": "Save password file",
            f"{MENU_DUMP}": "Print the encrypted password list (for testing)",
            f"{MENU_QUIT}": "Quit program"
        }
        for k, v in menu.items():
            print(f"   {k}. {v}")
        return self.get_option("Please enter a number", [1, len(menu)])


class Encryption(Storage):
    """
        Abstract out the crypto stuff so it is easier to replace with an
        actual encryption algorithm.
    """
    encryption_key = 0

    key_space = [c for c in ascii_letters + digits + punctuation]

    def invert_key(self, n: int) -> int:
        """
            return the additive inverse of a number.
        """
        try:
            # Cast n to int to ensure type correctness or error.
            return -1 * int(n)
        except ValueError:
            print("invert_key(n) expects integer input.")

    def get_char_from_keyspace(self, n: int):
        """
            return character from key_space character set at position n,
            where n is potentially greater than the size of the key space
            and the position must be wrapped around the "wheel" of the
            caesar cipher.
        """
        if n < 0:
            p = n
            while abs(p) > len(self.key_space):
                # p+=keyspace is subtracting key_spaces
                # to rotate over the wheel the number of
                # whole rotations.
                p += len(self.key_space)
                # At this point p is a fraction of the key_space 'cylinder'
            # we can return the character at that offset, a negative number.
            return self.key_space[p]
        elif n >= len(self.key_space):  # overflow
            # Get position from head recursively deducting the length of
            # the key_space until we are within bounds.  This essentially
            # loops over the 'cylinder' of the key_space until we arrive
            # at the desired character.
            return self.get_char_from_keyspace(n - len(self.key_space))
        else:  # simple within range
            return self.key_space[n]

    def caeser_cipher(self, message: str):
        """
            Perform a Caesar Cipher for demonstration purposes.  Note: this
            function can be used for encryption and decryption.

            For encryption, we provide a key and for decryption we simply
            provide the additive inverse key.  Thus, to encrypt key might be
            10, but to decrypt, the key would be -10.
        """
        output = ''
        for symbol in message:
            try:
                assert symbol in self.key_space, \
                    "symbol/char not found in key_space."
                output += self.get_char_from_keyspace(
                    self.encryption_key + self.key_space.index(symbol))
            except AssertionError as e:
                print(f"Encountered invalid character in message. {e}")
        return output

    def set_encryption_key(self):
        """
            Prompt the user to change the encryption key.  Note: if the user
            does this, previously encrypted information will become
            unintelligible as the old key will have encoded the information
            differently.  This can be used to demonstrate key-rotation
            problems.
        """
        while True:
            i = input(
                "Set encryption key (blank to exit, 'random' to "
                "generate random key): ")
            if i.strip() == "":
                print("Exiting with no change.")
                return  # Exit no change
            elif i.strip().lower() == "random":
                self.encryption_key = randint(0, 4096)
                break  # Acceptable change
            else:
                try:
                    self.encryption_key = int(i)
                    break  # Acceptable change
                except ValueError:
                    print("Invalid encryption key.  Key must be numeric.")
                    continue  # Invalid input...try again.
        print(f"New key set: {self.encryption_key}")


class Application(Encryption, Menu):
    """
        Demonstration Caesar Cipher Password Saver application.
        (This is not a secure solution. It is for demonstration only.)
    """

    def dump_passwords(self):
        """
            Dump the current in-memory password cache (dict) to the screen.
        """
        print("Print out the password list")
        self.cache.pretty_print()
        print()

    def add_password(self):
        """
            Prompt the user for a new password key-value pair and store
            the same in the in-memory cache (dict).  The new value is not
            persisted to disk and is volatile at this point.
        """
        print("Add New Password")
        site = input("What is this password for? ")
        self.cache.set(site, self.caeser_cipher(input("Enter the password: ")))
        print(f"Password added for {site}")

    def delete_password(self):
        """
            Delete a key-value password record from the in-memory cache (dict)
            and persist the cache to disk (overwriting any persisted copy of
            the record).
        """
        print("Delete Password")
        query = input("Which website are you searching for? ")
        print(f"Deleting password for {query}")
        if self.cache.delete(query):
            self.save()
        else:
            print(f"{query} not found.")

    def password_lookup(self):
        """
            Search the in-memory cache for a given password key (record name)
            and return the decrypted password in clear text.
        """
        query = input("Which website are you searching for? ")
        if self.cache.exists(query):
            print(self.caeser_cipher(self.cache.get(query),
                                     self.invert_key(self.encryption_key)))
        else:
            print(f"Record not found for {query}")

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == MENU_SET_KEY:
                self.set_encryption_key()
            elif choice == MENU_SET_FILE:
                self.set_file_name()
            elif choice == MENU_OPEN_FILE:
                self.load()
            elif choice == MENU_SEARCH:
                self.password_lookup()
            elif choice == MENU_ADD:
                self.add_password()
            elif choice == MENU_DELETE:
                self.delete_password()
            elif choice == MENU_SAVE:
                self.save()
            elif choice == MENU_DUMP:
                self.dump_passwords()
            elif choice == MENU_QUIT:
                print("Terminating.")
                sys.exit(0)
            else:
                print("Internal Error: Unknown or unrecognized option.")
            print("\n")


if __name__ == "__main__":
    app = Application()
    app.run()
