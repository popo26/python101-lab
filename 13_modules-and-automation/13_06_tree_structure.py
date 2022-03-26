# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path, WindowsPath
# import pathlib

# p = Path()

# path = p.cwd()
# print(path)

# win_path = WindowsPath("C:/Users/Ai/Documents/_CodingNomads/101-lab")
# print(win_path)

file_04 = WindowsPath("C:/Users/Ai/Documents/_CodingNomads/101-lab/04_build-something")
# print(file_04)

for filepath in file_04.iterdir():
    print(filepath.name)


