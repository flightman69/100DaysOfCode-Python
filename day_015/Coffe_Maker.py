from os import name, system
from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
        "water":500,
        "milk":500,
        "coffee":120,
        }

profit = 0
total_coffes_made = {"espresso": 0, "latte": 0, "cappuccino": 0}

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def check_availability(coffee):
    ingre = MENU[coffee]["ingredients"]

    item_left_value = []
    for item in ingre:

        item_left = resources[item] // ingre[item]
        item_left_value.append(item_left)

    return min(item_left_value)
def report():
    print("\nResource Left: ")
    for res in resources:
        print(f"{res}: {resources[res]}")
    print()

    can_make = {}
    for coffee in MENU:
        can_make[coffee] = check_availability(coffee)
    print("This resources is enough to make: ")
    for _ in can_make:
        print(f"{_}: {can_make[_]} (OR)")
    print()

    global profit
    print(f"Total profit made: ${profit}")
    print(f"Total coffees made: {total_coffes_made}")


def calc_payment():
    print(f"Please pay your bill in coins ${coffee_cost}")

    coins_value = {"penny": 0.01,"dime": 0.05,"cent": 0.10, "quater": 0.25}
    tot = 0
    for coin in coins_value:
        tot += int(input(f"{coin}: ")) * coins_value[coin]
    return tot


def make_coffee(coffee,coffee_cost,coffee_ingredients):
    is_available = check_availability(coffee)
    if is_available == 0:
        return 1
    payment = calc_payment()     
    if payment < coffee_cost:
        return payment
    elif payment > coffee_cost:
        balance = payment - coffee_cost
        print(f"Thank you for your payment ${payment:.2f} here's your balance: ${balance:.2f}")
        
        ingre = MENU[coffee]["ingredients"]
        item_left_value = []
        for item in ingre:
            resources[item] -= ingre[item]
        global profit
        profit += coffee_cost

        total_coffes_made[coffee] += 1
        return 0 


while True:
    
    clear()
    print(logo)
    print()
    user_input = input("Choose your energy cup (espresso/latte/cappuccino): ").lower()
    
    if user_input == 'report':
        report()
        input("Press Enter to continue: ")
    elif user_input == 'exit':
        print("Have a great day ☕")
        break
    else:
        coffee = user_input
        coffee_cost = MENU[user_input]["cost"]
        coffee_ingredients = MENU[user_input]["ingredients"]

        status = make_coffee(coffee,coffee_cost,coffee_ingredients)
        if status == 1:
            print(f"Insufficient resources to make {coffee}\n")
        elif  status == 0:
            print(f"Here's your {coffee} ☕. Enjoy it and have a great day\n")
        else:
            print(f"The amount ${status} is not enough.\n")
        input("Press Enter to continue") 
