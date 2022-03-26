# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib

path = pathlib.Path(r"C:\Users\Ai\Downloads\practice_folder")
new_path = pathlib.Path(r"C:\Users\Ai\Downloads\new_practice_folder")
new_path.mkdir()

for filepath in path.iterdir():
    if filepath.suffix == ".txt":
        new_filepath = new_path.joinpath("new" + filepath.name)
        filepath.replace(new_filepath)
        
