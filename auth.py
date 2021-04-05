import random
from shared import clear


generated_ids = []


def generate_id():
	'''
	Returns a random id
	'''
	return random.randrange(100_000_000, 1_000_000_000)


def generate_unique_id():
	'''
	Returns a random unique user id
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

	'''
	clear()
	print("\nBANK ACCOUNT CREATION PROCESS")
	print("******************************")
	print("Please provide your account details below.")

	try:
		firstname = input("\n\nEnter your first name: ")
		lastname = input("\nEnter your last name: ")
		email = input("\nEnter your email address: ")
		password = input("\nEnter your password: ")
	except:
		ptint("\n\nThere was an error while processing your inputs!!!")
		print("Press any key to proceed: ")
		signup()

	userid = generate_unique_id()


def login():
	'''

	'''

	pass
