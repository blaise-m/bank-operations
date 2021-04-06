from shared import clear, error_response
from datetime import datetime
from shared import complaints
from client import ClientComplaint


def dashboard(client):
	'''
	Displays client summary details after login
	'''
	clear()
	print("\nUSER DASHBOARD")
	print("**************")
	print(f"\nWelcome {client.get_firstname()} {client.get_lastname()}. Logged in on {datetime.now().strftime('%c')}")
	print(f"Your account balance is ${client.get_balance():,.2f}")
	
	response = input("\n\nPress Enter to proceed or 0+Enter to Exit: ")

	if response == "0": exit()

	user_menu(client)


def user_menu(client):
	'''
	Displays user menu and prompts user 
	to select a menu item
	'''
	clear()
	print("\nUSER ACCOUNT MENU")
	print("******************")
	print("\n1. DEPOSIT FUNDS")
	print("2. WITHDRAW FUNDS")
	print("3. MANAGE ACCOUNT DETAILS")
	print("4. MANAGE COMPLAINTS")
	print("5. EXIT")

	try:
		response = int(input("\n\nPlease select an option to proceed: "))
	except:
		error_response(user_menu)

	if response == 1:
		deposit(client)
	elif response == 2:
		withdraw(client)
	elif response == 3:
		manage_account(client)
	elif response == 4:
		manage_complaint(client)
	elif response == 5:
		exit()
	else:
		print("\n\nInvalid option selected. Enter number from 1 to 5")
		input("Press Enter to continue: ")
		user_menu()


def deposit(client):
	'''
	Takes in a client, prompts them for an amount to deposit
	and updates their account balance with the amount deposited
	'''
	clear()
	print("\nDEPOSIT SUB-MENU")
	print("*****************")
	print(f"Your account balance is ${client.get_balance():,.2f}")

	try:
		amount = float(input("\n\nPlease enter the amount to deposit: "))
	except:
		error_response(deposit, client)

	response = client.deposit(amount)

	if response['success']:
		print(f"Successfully deposited ${amount:,.2f}")
		print(f"Your new account balance is ${response['balance']:,.2f}")
		input("\n\nPress Enter to proceed: ")
		user_menu(client)
	else:
		print(f"Error: {response['error']}!!!")
		input("\n\nPress Enter to proceed: ")
		deposit(client)


def withdraw(client):
	'''
	Takes in a client, prompts them for an amount to withdraw
	and updates their account balance with the amount withdrawn
	'''
	clear()
	print("\nWITHDRAW SUB-MENU")
	print("*****************")
	print(f"Your account balance is ${client.get_balance():,.2f}")

	try:
		amount = float(input("\n\nPlease enter the amount to withdraw: "))
	except:
		error_response(withdraw, client)

	response = client.withdraw(amount)

	if response['success']:
		print(f"Successfully withdrawn ${amount:,.2f}")
		print(f"Your new account balance is ${response['balance']:,.2f}")
		input("\n\nPress Enter to proceed: ")
		user_menu(client)
	else:
		print(f"Error: {response['error']}!!!")
		input("\n\nPress Enter to proceed: ")
		withdraw(client)


def manage_account(client):
	'''
	Displays client details and allows the client to
	edit the editable details like password and email
	'''
	clear()
	print(f"\n{client.get_firstname().upper()} {client.get_lastname().upper()} USER PROFILE")
	print("************************************")
	print(f"\n1. FIRST NAME:                   {client.get_firstname().title()}")
	print(f"2. LAST NAME:                    {client.get_lastname().title()}")
	print(f"3. EMAIL (Editable):             {client.get_email()}")
	print(f"4. USER ID:                      {client.get_userid()}")
	print(f"5. PASSWORD (Editable):          {client.get_password()}")
	print(f"6. ACCOUNT BALANCE:              {client.get_balance()}")

	try:
		response = int(input("\n\nPress Enter to proceed, 3+Enter to update Email, 5+Enter to update password or 0+Enter to exit: "))
	except:
		user_menu(client)

	if response == 3:
		new_email = input("Enter the new Email address: ")
		client.update_email(new_email)
		manage_account(client)
	elif response == 5:
		new_password = input("Enter the new Password: ")
		client.update_password(client.get_password(), new_password)
		manage_account(client)
	elif response == 0:
		exit()
	else:
		user_menu(client)


def manage_complaint(client):
	'''
	Takes in a client and displays the complaints the client has submitted
	'''
	clear()
	print(f"\n{client.get_firstname().upper()} {client.get_lastname().upper()} COMPLAINTS FILE")
	print("************************************")

	client_complaints = complaints[client.get_userid()]

	if client_complaints:
		print("\nPlease see below a list of your complaints on file:\n")

		for index, complaint in enumerate(client_complaints):
			print(f"{index+1}. {complaint}")
	else:
		print("\nYou currently don't have any complaints on file.")

	try:
		response = int(input("\n\nPress Enter to proceed, 1+Enter to submit a complaint or 0+Enter to exit: "))
	except:
		user_menu(client)

	if response == 1:
		complaint_message = input("\nPlease enter your Complaint:\n")
		new_complaint = ClientComplaint(client, complaint_message)
		complaints[client.get_userid()].append(new_complaint)
		manage_complaint(client)
	elif response == 0:
		exit()
	else:
		user_menu(client)
