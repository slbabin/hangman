word = "test"
current_word = "-" * len(word)
print(f"The chosen word is: {current_word}")
mistakes = 0
letters = ""

while not(word == current_word or mistakes > 6):
    print(f"Word: {current_word}")
    print(f"Mistakes: {mistakes}")
    print(f"Added letters: ", end="")
    if len(letters) == 0:
        print("-")
    else:
        print(*letters)
    new_letter = input("Enter a letter: ").lower()
    

