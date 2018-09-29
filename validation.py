

""" 
will store user data as a list
"""

import re
user_data_base = []

class Register_user(object):
    def __init__(self,email,password):
        self.password = password
        self.email = email
            
    def validate_email (self,email):
        if not (re.search("@",email) and (re.search(".com",email))):
            return False
        else:
            return True

    def validate_age (self,user_age):
        pass

    def validate_username(self,userName):        
        username_length = len(userName)
        name_of_user = "henry"
        if name_of_user != userName and username_length > 4:
            print ("True")
        else:
            print ("false")

    def validate_password (self,password):
        capital_letter = (re.search("A-Z",password))
        small_letter = (re.search("a-z",password))
        less_characters  = (len(password) > 4)
        digit = (re.search("0-9",password))
        special_char =  (re.search("$#@",password))

        if  (capital_letter and small_letter and less_characters and digit and special_char):
            return True
        else:            
            return False


# email = "johndoemail.com"
# password = "HeN0@1"
# user = Register_user(email)
# user.validate_email(email) # works well
# user.validate_password(password) # our working well

