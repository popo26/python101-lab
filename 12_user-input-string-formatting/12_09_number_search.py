# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

choice = int(input("Pick a number between 0 and 1000000000.:  "))

is_running = True
while is_running:
    for n in range(0, 1000000000):
        if choice == n:
            print(n)
            is_running = False
            break
            
            
