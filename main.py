#!/usr/bin/python3

# Main.py
# ...
# 23/03/22

print('''Welcome to Cowsays What CTF!! 

You'll have 15 questions to complete, use google, a debian based lnux distro and a bash CLI.

For help, press 'h', to see question again, press 'q'.

Enjoy!

''')

userInput = input('Input: ')
while True:
	while True:
		if userInput == 'h' or 'H':
			print(userInput)
			break
		elif userInput == 'q' or 'Q':
			print(userInput)
			break
		else:
			userInput = input('Input: ')

	userInput = input('Input: ')
