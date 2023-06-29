# The Hangman game

Hangman is a popular word-guessing game that plays in the terminal window on Heroku. The game based on the standard rules of hangman where a random word is chosen by computer. The word is hidden by dashes and the player needs to reveal the word by guessing letters one by one. 
The game involves a gallows-shaped drawing and for each incorrect guess, a body part of a stick figure is drawn on the gallows. The player has 7 tries before the game finishes.

![Screenshot of how the site looks on different screen sizes](images/responsive-layout.jpg)

The live version of this game is located [here](https://hangman-1-5c8273b47be1.herokuapp.com/). 


## Features
- The game start with the generated banner and greetings.

    ![Screenshot of the Product links section](images/greeting.jpg) 


- The game prompts the player to enter their name. If no name is entered, the game assigns the name ANONIMUS to the player.

- After the user entered their name, the game displays player's name and the rules of the game. 

    ![Screenshot of the Product links section](images/rules.jpg) 
   

- The game selects a random word from the txt file. If the list is empty, show the message and exit the game.  

- The game dispays empty gallows, current secret word state hidden with dashes, amount of mistakes, and a list of entered letters. 

- The game promts the player to guess a letter. 

- Input validation and error checking
  - The game accepts only a single latin letter. If unsupported symbol or letter is entered, the game prompts to enter only one latin letter.  
  - With each entered letter, the games checks if it exists in the word. If the letter exists, the dash in the hidden word is replaced with this letter.
  - If a word is not guessed, and mistakes less than 7, gallows adds a part of the stick man body and the mistakes counter incremented.
  - At the end of the game, the player is asked if they want to play again. They need to enter Yes or No. If a wrong value is entered, the message is displayed that they need to enter the correct value.  



## Progam logic diagram   

![Screenshot of the Product links section](images/diagram-1.png) 

## Design 



## Testing and Validation

 __User Actions__


## Deployment


## Technologies Used
Languages Used



Programs Used


## Credits
 