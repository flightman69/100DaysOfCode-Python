from art import logo
from os import name,system

bidding_list = []
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def add_bidders():
	print(logo)
	print("="*20)

	name = input("Name of the bidder: ")
	amount = int(input("Bid amount: $")) 
	new_bidder = {}
	new_bidder["bidder_name"] = name
	new_bidder["bidding_amt"] = amount
	bidding_list.append(new_bidder)

	more_bidders = input("Anymore bidders[y/n]: ")
	if more_bidders == 'y':
		clear()
		add_bidders()

clear()
add_bidders()
highest_bid = 0
highest_bidder = ""
for bidder in bidding_list:
		amt = bidder["bidding_amt"]
		if amt > highest_bid:
			highest_bid = amt
			highest_bidder = bidder["bidder_name"]
clear()
print(logo)
print(f"The Highest Bidder is {highest_bidder} and the amount is ${highest_bid}") 


