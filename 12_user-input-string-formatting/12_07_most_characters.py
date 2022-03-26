# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings



one = input("Enter first string.: ")
two = input("Enter second string.: ")
three = input("Enter thrid string.: ")

comparison_list = [one, two, three]

x = max(comparison_list)
print(x)




