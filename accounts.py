
# creating a dictionary for user name and password
accounts = {}
# accounts = {'henry':'moga'}
class User_Accounts ():
    # get user inputs
    def add_account (self,User_name,password):
        # store the User name and Password into a dictionary
        accounts[User_name] = password
        print (accounts)



    def log_in(self,name, password):
        """
        this allows the user to log in if the 
        name and password entered are correct 
            
        """
        key, value = password, name

        if key in accounts and value == accounts[key]:
            print("\tLog in well...")
            # print (key)
            # print (value)
            return True

        else:
            print("\t Invalid credentials...")
            return False
