# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. 
# They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game

is_game_on = True
sword = 0
life = 1
user_name = input("What is your name?: ").lower()
print(f"Welcome {user_name.capitalize()} to the game world! ")
door_choice = input("left or right, which door would you like?: ").lower()
print(f"Current life is {life}. sword is {sword}")

while is_game_on:
    if door_choice == "left":
        return_choice = input("It's a empty room. Would you like to go back to the previous room? Yes or No: ").lower()
        if return_choice == "yes":
            door_choice = input("left or right, which door would you like?: ").lower()
        else:
            sword_choice = input("Look around. There is a sword. Would you like to TAKE IT or LEAVE IT?: ")
            if sword_choice == "take it":
                sword += 1
                print("Now you have 1 sword.")
                print(f"Current life is {life}. sword is {sword}")
            elif sword_choice == "leave it":
                print("OK.")
                door_choice = input("left or right, which door would you like?: ").lower()
            elif sword_choice != "take it" or "leave it":
                sword_choice2 = input("Sorry I don't understand. enter 'LEAVE IT' or 'TAKE IT':" )
                if sword_choice2 == "take it":
                    sword += 1
                    print("Now you have 1 sword.")
                elif sword_choice2 == "leave it":
                    print("OK.")
                    door_choice = input("left or right, which door would you like?: ").lower()
                
    elif door_choice == 'right':
        return_choice = input("There is a dragon! Woudl you like to go back to the previuos room? Yes or No: ").lower()
        if return_choice == "yes":
            door_choice = input("left or right, which door would you like?: ").lower()
        elif return_choice == "no":
            fight_choice = input("Are you gonna fight with the dragon?: ").lower()
            if fight_choice == 'yes':
                if sword >= 1:
                    print("You killed the dragon!")
                    life += 1
                    print(f"Current life is {life}. sword is {sword}")
                    is_game_on = False
                    # another_try = input(f"You eared a new life. Now your life is {life}.\nWould you like to try again?: ").lower()
                    # if another_try == "yes":
                    #     print(user_name)
                    #     print(f"Current life is {life}. sword is {sword}")
                    # else:
                    #     is_game_on = False

                if sword == 0:
                    print("You lost since you don't have any sword")
                    life -= 1
                    print(f"Current life is {life}. sword is {sword}")
                    if life >= 1:
                        print(f"You have {life} life left. Try again.\n{user_name}")
                    else:
                        is_game_on = False
            
            elif fight_choice == 'no':
                door_choice = input("left or right, which door would you like?: ").lower()

        


