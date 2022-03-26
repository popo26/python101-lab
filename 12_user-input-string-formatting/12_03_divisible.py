# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

choice = int(input("pick a number between 1 and 1,000,000,000: "))

if choice % 3 == 0:
    print(f"{choice} is divisible by 3.")
else:
    print(f"{choice} is not divisible by 3.")
