# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string_input = input("Type some words: ")
first_char = string_input[0]
print(string_input.replace(first_char, "&"))
