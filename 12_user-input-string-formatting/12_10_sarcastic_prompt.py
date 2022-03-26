# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

from typing import final


user_opinion = input("What is your honest opinion?: ")
final_sentense = ""

for char in user_opinion:
    if user_opinion.index(char) % 2 == 0:
        final_sentense += char.upper()
    else:
        final_sentense += char

print(final_sentense)
