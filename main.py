#!/usr/bin/python3

# Main.py
# ...
# 23/03/22
cq = '[Research] What linux program can make a cow say something?' # Current Question

print('''Welcome to Cowsays What CTF!! 
You'll have 15 questions to complete, use google, a debian based lnux distro and a bash CLI.
For help, enter 'help' if you need help, or enter 'hint' if you need a hint.

Question 0: ''' + cq)

ui = ' ' # User Input
qc = 0 # Question Counter
hc = 0 # Hint Counter
h = ' '
a = ' ' # Answer

# Main Game
while True:
	# Help + Hint Menu
	if ui == 'help' or ui == 'Help':
		print('[Help] You\'re up to Question ' + str(qc) + ': ' + cq)
	elif ui == 'hint' or ui == 'Hint':
		print('[Hint] ' + h + ' [Characters] ' + str((len(a))))
	# Questions
	# Q1
	if qc == 0:
		a = 'cowsay'
		h = 'cowsay what?'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you install the program?'
			print('Q' + str(qc) + ': ' + cq)
	# Q2
	elif qc == 1:
		a = 'sudo apt install cowsay'
		h = 'Debiasn-based systems: sudo <package manager> install <program>'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you execute (or run) the program?'
			print('Q' + str(qc) + ': ' + cq)
	# Q3
	elif qc == 2:
		a = 'cowsay'
		h = 'Type <program> and a message, use CTRL + C if needed. You may need to use /usr/games/<program>...'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'What other program was installed?'
			print('Q' + str(qc) + ': ' + cq)
	# Q4
	elif qc == 3:
		a = 'cowthink'
		h = 'List /usr/games - don\'t say, think.'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you access the manual page for this program?'
			print('Q' + str(qc) + ': ' + cq)
	# Q5
	elif qc == 4:
		a = 'man cowsay'
		h = 'man I wonder how...'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you make the cow moo'
			print('Q' + str(qc) + ': ' + cq)
	# Q6
	elif qc == 5:
		a = 'cowsay moo'
		h = '<program> <argument>'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'Using the man page, how do you have the cow moo and appear dead?'
			print('Q' + str(qc) + ': ' + cq)
	# Q7
	elif qc == 6:
		a = 'cowsay -d moo'
		h = 'Read the man page and use the - before a letter e.g. cowsay -h '
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'Using the same format, how do you make the cow moo and appear paranoid?'
			print('Q' + str(qc) + ': ' + cq)
	# Q8
	elif qc == 7:
		a = 'cowsay -p moo'
		h = 'Use the same format as you just did cowsay -<letter> moo'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'Using the same format, how do you make the cow moo and appear greedy?'
			print('Q' + str(qc) + ': ' + cq)
	# Q9
	elif qc == 8:
		a = 'cowsay -g moo'
		h = 'Use the same format as you just did cowsay -<letter> moo'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you display a list of other cows (if you can call them cows)?'
			print('Q' + str(qc) + ': ' + cq)
	# Q10
	elif qc == 9:
		a = 'cowsay -l'
		h = 'man, if only there was a help page!'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you make a dragon say raw?'
			print('Q' + str(qc) + ': ' + cq)
	# Q11
	elif qc == 10:
		a = 'cowsay -f dragon raw'
		h = 'man, if only there was a help page!'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you make a turtle say hello?'
			print('Q' + str(qc) + ': ' + cq)
	# Q12
	elif qc == 11:
		a = 'cowsay -f turtle hello'
		h = 'man, if only there was a help page!'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = 'How do you make the cow wink it\'s right eye and say moo?'
			print('Q' + str(qc) + ': ' + cq)
	# Q13
	elif qc == 12:
		a = 'cowsay -e -O moo'
		h = 'Use the - symbol and a captial O for the eyes string - there\'s a switch you need.'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			cq = '[Research] How do you make the cow\'s tounge look like this () and say moo?'
			print('Q' + str(qc) + ': ' + cq)
	# Q14
	elif qc == 13:
		a = 'cowsay -T \(\) moo'
		h = 'Hm, this is wiki hard.'
		ui = input('Answer Q' + str(qc) + ': ')
		if ui == a:
			print('[Answer] ' + a + ' - Good work!')
			qc +=1
			# cq = 'x'
			# print('Q' + str(qc) + ': ' + cq)
			break
print('Flag: cowsaysWhatCTF{M00_M3_P!3@$3} - Well done, you finished the CTF!')