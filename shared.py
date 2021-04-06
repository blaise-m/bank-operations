from os import system, name


generated_ids = []
clients = {}
complaints = {}


def clear():
	'''
	Clears screen for windows and linux
	Else does nothing
	'''
	try:
		if name == 'nt':
			system('cls')
		else:
			system('clear')
	except:
		pass


def error_response(callback, *args):
	'''
	Takes in a function to call when an error occurs
	Gives the user feedback when the error occurs and calls the function
	'''
	print("\n\nAn error occurred while processing your input!!!")
	input("Press Enter to proceed: ")
	callback(*args)
