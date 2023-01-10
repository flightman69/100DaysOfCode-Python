#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

event = random.randint(0,1)
outcome = "Heads"
if event == 0:
    outcome = "Tails"

print(outcome)
