import random

print("Welcome to Python Password generator!")

letters = 'abcdefghijklmnopqrstuvexyz'
letters = list(letters+letters.upper())
numbers = list('0123456789')
symbols = list('!@#$%^&*()?_')

nr_letters = int(input("How many Letters you want it to be: "))
nr_numbers = int(input("How many Numbers you want it to be: "))
nr_symbols = int(input("How many Symbols you want it to be: "))

password = []
for i in range(nr_letters+1):
	password.append(random.choice(letters)
for i in range(nr_numbers+1):
	password.append(random.choice(numbers)
for i in range(nr_symbols+1):
	password.append(random.choice(symbols)

password.shuffle()
final_password = ''.join(password)
print(f"Your random Password is {final_password}")

