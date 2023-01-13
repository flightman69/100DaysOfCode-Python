from os import name, system
from art import logo

def clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

operations = {
	'+': add,
	'-': sub,
	'*': mul,
	'/': div,
	}
def calc():
	print(logo)
	num1 = int(input("Number 1: "))

	while True:

		num2 = int(input("Number 2: "))
		for opr in operations.keys():
			print(opr)

		option = input("Pick an operation from the line above: ")
		function = operations[option]
		result = function(num1, num2)

		print(f"{num1} {option} {num2} = {result}")

		if input("continue with answer[y/n] : ") == 'y':
			num1 = result
			clear()
			print(logo)
			print(f"Previous answer is {result}")
		else:
			clear()
			calc()

calc()
