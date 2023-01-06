# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = (name1+name2).lower()
true = 0
love = 0

for i in "true":
    true += name.count(i)
for i in "love":
    love += name.count(i)
score = int(str(true) + str(love))

if score > 90 or score < 10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
