def ask():
	name = raw_input("What is your name: ")
	if name:
		print "Hi " + name
	else:
		print "Please enter a name "
		ask()

ask()