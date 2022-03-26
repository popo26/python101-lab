# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_input = input("Enter random words.:  ").lower()
 
a = user_input.count("a")
i = user_input.count("i")
u = user_input.count("u")
e = user_input.count("e")
o = user_input.count("o")

print(f"In your entry, there are {a} As, {i} Is, {u} Us, {e} E, {o} Os.")


