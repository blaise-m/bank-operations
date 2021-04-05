class ClientAccount():
	'''
	Used to generate client account objects
	Takes in userid, firstname, lastname, email and password
	As arguments
	'''

	def __init__(self, userid, firstname, lastname, email, password):
		self.userid = userid
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.password = password

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
		Updates the email of the client instance
		'''
		self.email = new_email

	def update_password(self, new_password):
		'''
		Updates the password of the client instance
		'''
		self.password = new_password

	def __repr__(self):
		'''
		Returns the string representation of
		the Object
		'''
		return f'{self.userid}: {self.firstname} {self.lastname}'
