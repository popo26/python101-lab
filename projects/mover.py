# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib
# Find the path to my Desktop
# path = pathlib.Path().cwd()
# print(type(path))
# print(str(path))
# x = pathlib.WindowsPath(r"C:\Users\Ai\Downloads")
x = pathlib.Path(r"C:\Users\Ai\Downloads")
print(x)

# Create a new folder

##list all files##

# for filepath in x.iterdir():
#     print(filepath.name)

##create a new folder##

new_path = pathlib.Path(r"C:\Users\Ai\Downloads\ZIP_FOLDER")
# new_path.mkdir()

# Filter for screenshots only

# for filepath in x.iterdir():
#     if filepath.suffix == ".zip":
#         print(filepath.name)



for filepath in x.iterdir():
    if filepath.suffix == ".zip":
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)

        # Move the screenshot there
        filepath.replace(new_filepath)
