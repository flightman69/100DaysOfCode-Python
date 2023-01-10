import random
import hangman_art
import hangman_words

stages = hangman_art.stages
hangman_logo = hangman_art.logo
words = hangman_words.word_list 

print(hangman_logo)
choosen_word = random.choice(words)
display = []
print(f"The Choosen Word is {choosen_word}")
for _ in choosen_word:
	display += '_'

end_of_game = False
lives = 6
print(f"Total Lives: {lives}")
while not end_of_game:
	print(stages[lives])
	user_guess = input("Enter Your guess: ").lower()	
	if user_guess in display:
		print(f"You've already guessed the letter {user_guess}")
	
	for ind in range(len(choosen_word)):
		letter = choosen_word[ind]
		if letter == user_guess:
			display[ind] = user_guess
	if user_guess not in choosen_word:
		print(f"The letter {user_guess} is not in the word")
		lives -= 1
		if lives == 0:
			end_of_game = True
			print("You've Lost")

	print("="*20+'\n')	
	print(' '.join(display))
	print(f"Lives left: {lives}")

	if '_' not in display:
		end_of_game = True
		print("You've Won")

