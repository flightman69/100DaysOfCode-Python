#Importing Random Module
#using random int 
#using random float
#creating our own module

import random
import printName

random_int = random.randint(1,10)
print(f"The Random Integer produced is {random_int}")
random_float = random.random() 
print(f"The Random Float produced is always from 0.0 - 1.0")
print(f"The Random Float produced in this example is {random_float}")

print(f"We can multiply an integer with this random float to get a range of random float numbers")
print(f"Here for example the random float is {random_int * random_float}")

print("Additional thing 'Importing/Creating our own module")

print("Here I created and imported a module called printName to print my name")

myname = printName.user_name
print(f"My name is {myname}")

