import string
import random

# Symbols
symbols = string.punctuation
print(symbols)

# Letters and Numbers for display
for letter in range(ord('A'), ord('z') + 1):
    print(chr(letter), end=" ")
for number in range(ord('0'), ord('9') + 1):
    print(chr(number), end=" ")
print("\nWelcome to Password Generator")

# User input for password requirements
n_letter = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

# Generating password
password_list = []

for i in range(n_letter):
    char = random.choice(string.ascii_letters)
    password_list+=(char)

for i in range(n_symbols):
    char = random.choice(symbols)
    password_list+=(char)

for i in range(n_numbers):
    char = random.choice(string.digits)
    password_list+=(char)

# Shuffle the password list to make it more random
random.shuffle(password_list)

# Convert the list to a string22
password = ''.join(password_list)
print(f"Generated password: {password}")
