class ClientAccount():
	'''
	Used to generate client account objects
	Takes in userid, firstname, lastname, email and password
	As arguments
	'''

	def __init__(self, userid, firstname, lastname, email, password):
		'''
		Class constructor
		'''
		self.__userid = userid
		self.__firstname = firstname
		self.__lastname = lastname
		self.__email = email
		self.__password = password
		self.__balance = 0

	def get_userid(self):
		'''
		Returns the userid of the client instance
		'''
		return self.__userid

	def get_firstname(self):
		'''
		Returns the firstname of the client instance
		'''
		return self.__firstname

	def get_lastname(self):
		'''
		Returns the lastname of the client instance
		'''
		return self.__lastname

	def get_email(self):
		'''
		Returns the email of the client instance
		'''
		return self.__email

	def get_password(self):
		'''
		Returns the password of the client instance
		'''
		return self.__password

	def get_balance(self):
		'''
		Returns the balance of the client instance
		'''
		return self.__balance

	def update_email(self, new_email):
		'''
		Takes in the new email
		Updates the old email of the client instance
		with the new email
		'''
		self.__email = new_email
		return {'success': True, 'email': self.__email}

	def update_password(self, old_password, new_password):
		'''
		Takes in the old password and new password
		Updates the old password of the client instance
		with the new password
		'''
		if old_password == self.__password:
			self.__password = new_password
			return {'success': True, 'password': self.__password}
		else:
			return {'success': False, "error": "Invalid Password"}

	def deposit(self, amount):
		'''
		Takes in an amount and updates the account balance
		if the amount is positive
		'''
		if amount >= 0:
			self.__balance += amount
			return {'success': True, 'balance': self.__balance}
		else:
			return {'success': False, "error": "Negative amount deposited"}

	def withdraw(self, amount):
		'''
		Takes in an amount and updates the balance
		if the amount is positive and less than or equal
		to the account balance 
		'''
		if (amount >= 0) and (amount <= self.__balance):
			self.__balance -= amount
			return {'success': True, 'balance': self.__balance}
		else:
			return {'success': False, "error": "Negative amount or Insufficient funds"}

	def __repr__(self):
		'''
		Returns the string representation of
		the Client Account Object
		'''
		return f'{self.__firstname} {self.__lastname}'


class ClientComplaint():
	'''
	Used to generate client complaint objects
	Takes in a client and a complaint
	'''

	def __init__(self, client, complaint):
		'''
		Class constructor
		'''
		self.__client = client
		self.__complaint = complaint
		self.__status = "Pending"

	def get_client(self):
		'''
		Returns the client owning the complaint
		'''
		return self.__client

	def get_complaint(self):
		'''
		Returns the body of the complaint
		'''
		return self.__complaint

	def get_status(self):
		'''
		Returns the status of the complaint
		'''
		return self.__status

	def mark_resolved(self):
		'''
		Updates the status of the complaint to resolved
		'''
		self.__status = "Resolved"
		return {'success': True, 'status': self.__status}

	def __repr__(self):
		'''
		Returns the string representation of
		the Client Complaint Object
		'''
		return f'{self.__complaint}'
