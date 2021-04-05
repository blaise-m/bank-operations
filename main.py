from shared import clear, error_response
from auth import signup, login


def init():
	'''
	Serves as the landing page for the app
	Displaying the Welcome greeting to the user
	'''
	
	clear()

	print("\nBANKING MENU OPTIONS")
	print("********************")
	print("For your self-service menu, we have the following options:")
	print("\n1. SIGNUP  (If you are new and have no Account)")
	print("2. LOGIN  (If you already have an Account)")
	print("3. EXIT  (To exit the system)")

	try:
		response = int(input("\n\nPlease select an option to proceed: "))
	except:
		error_response(init)
		
	if response == 1:
		signup()
	elif response == 2:
		login()
	elif response == 3:
		exit()
	else:
		print("You have entered an invalid input. Valid options are 1, 2 or 3")
		input("\n\nPlease press any key to proceed: ")
		init()


if __name__ == "__main__":

	clear()

	print("\nBLAZE BANK LTD CLIENT ATM")
	print("**************************")
	print("\nDear esteemed client, welcome to BLAZE Bank ATM")
	print("Please sit back and feel at home while we diligently serve you!!")	
	input("\n\nPress any key to continue: ")

	init()
