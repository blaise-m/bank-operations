from os import system


def clear():
	'''
	Clears screen for windows and linux
	Else does nothing
	'''
	try:
		system('clear')
	except:
		pass


def error_response(callback):
	'''
	Takes in a function to call when an error occurs
	Gives the user feedback when the error occurs and calls the function
	'''
	print("\n\nAn error occurred while processing your input!!!")
	input("Press any key to proceed: ")
	callback()
