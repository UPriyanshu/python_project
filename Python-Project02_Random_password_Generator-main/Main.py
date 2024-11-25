import os
import random
import string

def generate_password(length):
    # Define possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for the desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Please enter a positive integer for the password length.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
