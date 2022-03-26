# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

game_is_on = True
num_of_tries = 3

random_number = random.randint(1, 10)

while game_is_on:
    user_choice = int(input("Pick a number between 1 and 10:  "))
    if user_choice == random_number:
        print("Correct!")
        game_is_on = False
    else:
        print("Wrong!")
        print(random_number)
        num_of_tries -= 1
        if num_of_tries == 0:
            game_is_on = False
        