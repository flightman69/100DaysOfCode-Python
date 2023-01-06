print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = tot_bill*(tip_percent/100)
bill_plus_tip = tot_bill + tip
each_should_pay = bill_plus_tip/people
each_should_pay = round(each_should_pay,2)
print(f"Each person should pay: ${each_should_pay:.2f}")
