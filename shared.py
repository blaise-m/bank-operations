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