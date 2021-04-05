from shared import clear
from datetime import datetime


def dashboard(client):
	'''
	Displays client summary details after login
	'''
	clear()
	print("\nUSER DASHBOARD")
	print("**************")
	print(f"\nWelcome {client.get_firstname} {client.get_lastname}. Logged in on {datetime.now().strftime('%c')}")
	print(f"Your account balance is ${client.balance}")
