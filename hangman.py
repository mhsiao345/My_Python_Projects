import random

import hangman_words
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.

import hangman_art
print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

#If player has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f'{guess} has already been guessed.')

#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
                # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

#Check if wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

#Check if player has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])