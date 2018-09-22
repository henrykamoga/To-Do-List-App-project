"""
Author :: kamoga Henry
Tell :: 0701243139

"""

# creating a dictionary for user name and password
accounts = {}
# get user inputs
def add_account (User_name,password):
	# store the User name and Password into a dictionary
	accounts[User_name] = password



def log_in(name, password):
	"""
	this allows the user to log in if the 
	name and password entered are correct 
		
	"""

	key, value = password, name
	# print (accounts)
	# print (name in accounts)
	# print (password == accounts[name])

	if key in accounts and value == accounts[key]:
		print("\tLog in well...")
		return True

	else:
		print("\t Invalid credentials...")
		return False
