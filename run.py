GAME_NAME = "HANGMAN"
DEFAULT_NAME = "ANONIMUS"
ALPHABET = "ABDEFGHIJKLMNOPQRSTUVWXYZ"

x = (39 - len(GAME_NAME)) // 2
y = 1 if len(GAME_NAME)%2 == 0 else 0

print("* " * 20 + "*")
print("*" + " " * 40 + "*")
print("*" + " " * x + GAME_NAME.upper() + " " * (x + y) + "*")
print("*" + " " * 40 + "*")
print("* " * 20 + "*")
print()

want_to_play = True
guessed = 0
missed = 0

while want_to_play:
    word = "SUPER"
    current_word = "-" * len(word)
    print(f"The chosen word is: {current_word}\n")
    mistakes = 0
    letters = ""
    
    while not (word == current_word or mistakes > 6):
        print(f"Word: {current_word}")
        print(f"Mistakes: {mistakes} out of 7")
        print(f"Added letters: ", end="")
        

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
            
            if new_letter == word[i]:  # checking if a letter exists in the word
                current_word = current_word[:i] + new_letter + current_word[i + 1:]
                letter_in_word = True

        if not letter_in_word:
            mistakes += 1
        if not new_letter in letters:
            letters += new_letter

    print()
    print(f"Word: {current_word}")
    print(f"Mistakes: {mistakes} out of 7")
    print(f"Added letters: ", end="")

    if len(letters) == 0:
        print("-")
    else:
        print(*letters)

    if word == current_word:
        print("Congratulations! You guessed the word!")
        guessed += 1
    else:
        print("Sorry, but didn't guess the word.") 
        missed += 1   

    print(f"The correct word is: {word}") 


    play_again = input("Do you want to play again? ")
    while not(play_again == "yes" or play_again == "no"):
        play_again = input("Just enter \"Yes\" or \"No\": ").lower()
    if play_again == "no":
        want_to_play = False
print()
print("Thank you for your game!")    
print(f"You guessed {guessed} word, and you missed {missed} words.")
input("Click Enter to finish the game.")