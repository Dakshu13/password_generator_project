import random
# This functionality is used for shuffle the items in the list
from random import shuffle

# create a self made data for each list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Welcome the viewers with print statement
print("Welcome to the PyPassword Generator!")
#ask input from the user to add the numbers of letters,symbols and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# For easy password such as the letters,numbers,symbols comes in order!
#password = " "

#for l in range(0, nr_letters):
 #   password += random.choice(letters)
#for l in range(0, nr_symbols):
  #  password += random.choice(symbols)
#for l in range(0, nr_numbers):
 #   password += random.choice(numbers)

#print(password)

# for hard password where the letters, numbers and symbols are shuffled!

password = []
for l in range(0, nr_letters):
    password += random.choice(letters)
for l in range(0, nr_symbols):
    password += random.choice(symbols)
for l in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

password_list = " "
for h in password:
    password_list += h

print(password_list)