# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

choice = input("Pick a number between 1 and 12: ").lower()

if choice == "1":
    print("January")
elif choice == "2":
    print("Feburary")
elif choice == "3":
    print("March")
elif choice == "4":
    print("April")
elif choice == "5":
    print("May")
elif choice == "6":
    print("June")
elif choice == "7":
    print("July")
elif choice == "8":
    print("August")
elif choice == "9":
    print("September")
elif choice == "10":
    print("October")
elif choice == "11":
    print("November")
elif choice == "12":
    print("December")
else:
    print("It's not a valid number here.")


