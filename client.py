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
		self.userid = userid
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.password = password
		self.balance = 0

	def get_userid(self):
		'''
		Returns the userid of the client instance
		'''
		return self.userid

	def get_firstname(self):
		'''
		Returns the firstname of the client instance
		'''
		return self.firstname

	def get_lastname(self):
		'''
		Returns the lastname of the client instance
		'''
		return self.lastname

	def get_email(self):
		'''
		Returns the email of the client instance
		'''
		return self.email

	def get_password(self):
		'''
		Returns the password of the client instance
		'''
		return self.password

	def update_email(self, new_email):
		'''
		Takes in the new email
		Updates the old email of the client instance
		with the new email
		'''
		self.email = new_email
		return {'success': True, 'email': self.email}

	def update_password(self, old_password, new_password):
		'''
		Takes in the old password and new password
		Updates the old password of the client instance
		with the new password
		'''
		if old_password == self.password:
			self.password = new_password
			return {'success': True, 'password': self.password}
		else:
			return {'success': False, "Error": "Invalid Password"}

	def deposit(self, amount):
		'''
		Takes in an amount and updates the account balance
		if the amount is positive
		'''
		if amount >= 0:
			self.balance += amount
			return {'success': True, 'balance': self.balance}
		else:
			return {'success': False, "Error": "Negative amount deposited"}

	def withdraw(self, amount):
		'''
		Takes in an amount and updates the balance
		if the amount is positive and less than or equal
		to the account balance 
		'''
		if (amount >= 0) and (amount <= balance):
			self.balance -= amount
			return {'success': True, 'balance': self.balance}
		else:
			return {'success': False, "Error": "Negative amount or Insufficient funds"}

	def __repr__(self):
		'''
		Returns the string representation of
		the Object
		'''
		return f'{self.firstname} {self.lastname}'
