# Print out every prime number between 1 and 1000.

for num in range(1, 1001):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime == True: 
        print(f"{num} is prime")
