ALPHABET = "ABDEFGHIJKLMNOPQRSTUVWXYZ"

word = "test"
current_word = "-" * len(word)
print(f"The chosen word is: {current_word}")
mistakes = 0
letters = ""

while not (word == current_word or mistakes > 6):
    print(f"Word: {current_word}")
    print(f"Mistakes: {mistakes}")
    print(f"Added letters: ", end="")
    if len(letters) == 0:
        print("-")
    else:
        print(*letters)

    new_letter = input("Enter a letter: ").lower()
    while not (len(new_letter) == 1 and new_letter in ALPHABET):
        new_letter = input("Input only one latin letter: ").lower()
    for i in range(len(word)):
        no_such_letter = True
        if new_letter == word[i]:  # checking if a letter exists in the word
            current_word = current_word[0:1] + new_letter + current_word[i + 1:]
            no_such_letter = False
    if no_such_letter:
        mistakes += 1       
            
