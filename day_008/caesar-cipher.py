from art import logo
alphabet = list("abcdefghijklmnopqrstuvexyz"*2)

def caesar_cipher(direc,msg,shift):
	global alphabet
	cripted = ""
	if direc == 'E':
		for i in msg:
			if i in alphabet:
				encode = alphabet.index(i) + shift
				cripted += alphabet[encode]
			else:
				cripted += i
		print(f"The Encoded Message is {cripted}")
	else:
		for i in msg:
			if i in alphabet:
				decode = alphabet.index(i) - shift
				cripted += alphabet[decode]
			else:
				cripted += i
		print(f"The Decoded Message is {cripted}")


print(logo)
while True:
	direction  = input("Type E to encrypt, type D to decrypt: ").upper()
	text = input("Enter your message: ").lower()
	shift = int(input("Enter the Shift number: "))
	while shift >= 26:
		shift -= 26
	caesar_cipher(direction,text,shift)
	repeat = input("Repeat the program [y/n]: ") or 'n'
	if repeat == 'n':
		break
