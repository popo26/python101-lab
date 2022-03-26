

# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

import random

is_game_on = True
word_choices = ['flower', 'apple', 'orange']
random_word = random.choice(word_choices)
attempts = 5

display = []
# print(random_word)
for char in random_word:
    display += "_"
# print(display)

while is_game_on:
    user_guess = input("Guess a word: ").lower()
    print(f"You have {attempts} left.")

    for position in range(len(random_word)):
        letter = random_word[position]

        if letter == user_guess:
            display[position] = letter
    # print(display)
    print(" ".join(display))

    if "_" not in display:
        is_game_on = False
        (print("You win."))

    if user_guess not in random_word:
        attempts -= 1
        if attempts == 0:
            is_game_on = False
            print("You lose.")
        
    print(f"{attempts} attemps left")

    
    # for char in random_word_list:
    #     new_word = char.replace(char, "_")
    #     after_guessed_word_list.append(new_word)
    # print(after_guessed_word_list)
    
    # for index, char in enumerate(random_word_list):
    #     user_guess = input("Guess a word: ").lower()
    #     if user_guess == char:
    #         for char in after_guessed_word_list:
    #             new_word = char.replace(char, user_guess)
    #             after_guessed_word_list[int(index)] = new_word
    #         print(after_guessed_word_list)
    # user_guess = input("Guess a word: ").lower()
    # if char == user_guess:
    #     new_word = after_guessed_word_list.replace(char, user_guess)
    #     print(after_guessed_word_list)
        

 
            

    
    




