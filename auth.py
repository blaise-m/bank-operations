import random
from shared import clear, error_response, generated_ids, clients, complaints
from operations import dashboard
from client import ClientAccount


def generate_id():
	'''
	Returns a random id
	'''
	return random.randrange(100_000_000, 1_000_000_000)


def generate_unique_id():
	'''
	Returns a unique random id
	'''
	user_id = generate_id()

	while user_id in generated_ids:
		# User ids must be unique
		# So if we have already generated the id before
		# We generate another random id

		user_id = generate_id()

	generated_ids.append(user_id)
	# Above line keeps track of generated ids
	return user_id


def signup():
	'''
	Creates a client account and adds it to the client list
	Then invokes the login sequence
	'''
	clear()
	print("\nBANK ACCOUNT CREATION PROCESS")
	print("******************************")
	print("Please provide your account details below.")

	try:
		firstname = input("\n\nEnter your first name: ")
		lastname = input("Enter your last name: ")
		email = input("Enter your email address: ")
		password = input("Enter your password: ")
	except:
		error_response(signup)

	userid = str(generate_unique_id())
	client = ClientAccount(userid=userid, firstname=firstname, lastname=lastname, email=email, password=password)

	clients[userid] = client
	complaints[userid] = []
	print("\n\nCongratulations!! Your Account has been successfully created.")
	print(f"Your account number is {userid}. Please note it down since it is used for login")
	
	response = input("\n\nPress Enter to proceed and login or 0+Enter to Exit: ")

	if response == "0": exit()

	login()


def authenticate_user(account_number, password):
	'''
	Takes in an account number and password
	And authenticates them against the user database
	'''
	for account in clients.keys():
		valid_account = (account == account_number)
		valid_password = (clients[account].get_password() == password)

		if valid_account and valid_password:
			return True
		else:
			return False


def login():
	'''
	Authenticates a user against the user database
	And logs the user in
	'''
	clear()
	print("\nBANK ACCOUNT LOGIN PROCESS")
	print("***************************")
	print("Please provide your login details below.")

	try:
		account_number = input("\n\nEnter your account number: ")
		password = input("Enter your password: ")
	except:
		error_response(login)

	if authenticate_user(account_number, password):
		dashboard(clients[account_number])
	else:
		print("\n\nWrong account number or password!!!")
		
		try:
			response = input("Press Enter to try again, 1+Enter to create a new account or 0+Enter to Exit: ")
		except:
			error_response(login)

		if response == "0":
			exit()
		elif response == "1":
			signup()
		else:
			login()
