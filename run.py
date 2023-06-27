from random import shuffle  # Import the shuffle function from Random module
from sys import exit  # import function exit from module sys.

GAME_NAME = "HANGMAN"
DEFAULT_NAME = "ANONIMUS"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FILE_DATA = "words.txt"
BS = '\\'


def greeting_rules():
    """
    Display the game frame and rules.
    """
    x = (39 - len(GAME_NAME)) // 2
    y = 1 if len(GAME_NAME) % 2 == 0 else 0

    print("* " * 20 + "*")
    print("*" + " " * 39 + "*")
    print("*" + " " * x + GAME_NAME.upper() + " " * (x + y) + "*")
    print("*" + " " * 39 + "*")
    print("* " * 20 + "*")
    print()
    print(f"Welcome to the game \"{GAME_NAME}\"!\n")

    name = input("Enter your name! ")  # Prompt for the participant's name.
    print()

    if not name:
        # If no name entered, display the default name Anonimus.
        name = DEFAULT_NAME

    print(f"Hi {name}, the rules are easy! ")
    print("I'll pick a word and write how many letters in it")
    print("You need to guess a word by entering lettes one by one")
    print("You have 7 tries.")
    print()
    return name


words = []  # Empty list to hold words from a file


def read_file():
    file = open(FILE_DATA)
    for line in file:
        # Setting words to lower case and strip "/n" from the end.
        line = line.lower().strip()
        # Add a word from the file to the end of the list
        words.append(line)
    file.close()

    if len(words) == 0:
        print("There are no words in the file!")
        input("Click Enter to finish the game.")
        exit()

    shuffle(words)


def gallows(mistakes):
    """
    Display gallows
    """
    print(f"-------")
    print(f"|/   {'|' if mistakes > 0 else ' '}")
    print(f"|    {'o' if mistakes > 1 else ' '}")
    print(f"|   {'/' if mistakes > 3 else ' '}{'|' if mistakes > 2 else ' '}{BS if mistakes > 4 else ' '}")
    print(f"|   {'/' if mistakes > 5 else ' '} {BS if mistakes > 6 else ' '}")
    print(f"|")
    print(f"|__")
    print()


def play_game(name):
    want_to_play = True
    guessed = 0
    missed = 0
    while want_to_play:
        if len(words) == 0:
            print("Unfortunately, no more words in the file!")

        else:
            word = words.pop().upper()  # Gets the last entry from the list and
            # removes it from the list
            current_word = "-" * len(word)
            print(f"The chosen word consists of: {len(word)} letters.\n")
            mistakes = 0
            letters = ""

            while not (word == current_word or mistakes > 6):

                gallows(mistakes)
                print()
                print(f"Word: {current_word}")
                print(f"Mistakes: {mistakes} out of 7")
                print(f"Letters you tried: ", end="")

                if len(letters) == 0:
                    print("-")
                else:
                    print(*letters)
                new_letter = input("Enter a letter: ").upper()

                while not (len(new_letter) == 1 and new_letter in ALPHABET):
                    new_letter = input("Input only one latin letter: ").upper()

                print()
                letter_in_word = False

                for i in range(len(word)):
                    # checking if a letter exists in the word.
                    if new_letter == word[i]:
                        current_word = current_word[:i] + new_letter + current_word[i + 1:]
                        letter_in_word = True

                if not letter_in_word:
                    mistakes += 1
                if not new_letter in letters:
                    letters += new_letter

            gallows(mistakes)

            print()
            print(f"Word: {current_word}")
            print(f"Mistakes: {mistakes} out of 7")
            print(f"Added letters: ", end="")

            if len(letters) == 0:
                print("-")
            else:
                print(*letters)

            if word == current_word:
                print(f"{name}, congratulations! You guessed the word!")
                guessed += 1
            else:
                print(f"{name}, unfortunately, you didn't guess the word.")
                missed += 1

            print(f"The correct word is: {word}")

            play_again = input("Do you want to play again? ")
            while not (play_again == "yes" or play_again == "no"):
                play_again = input("Just enter \"Yes\" or \"No\": ").lower()
            if play_again == "no":
                want_to_play = False

            print()
    return guessed, missed


user = greeting_rules()
read_file()
x, y = play_game(user)
print("Thank you for your game! Below, you can see your results:")
print(f"You guessed {x} word, and you missed {y} words.")
