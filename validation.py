

""" 
will store user data as a list


test coverage
code climate
coveralls(coveralls.yml)
travis(travis.yml)


"""
import re
user_data_base = []

class Register_user:
    def __init__(self,name,email,password,username,age,gender):
        self.name = name
        self.password = password
        self.email = email
        self.username = username
        self.age = age
        self.gender = gender

    def validate_name (self,name):
        valide_name = type(int)
        if name != valide_name:
            print (" valid Name")
            return True

        if name == valide_name:
            print (" not valid Name")
            return False

    def validate_email (self,email):
        if not (re.search("@",email) and (re.search(".com",email))):
            return False
        else:
            return True

    def validate_password (self,password):
        password_char =  re.compile("((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,8})")
        required_password = password_char.match(password)
        special_char = re.search("@",password)
        if required_password and special_char:
            return True
        else:            
            return False

    def validate_username(self, name_of_user, userName):        
        required_length = len(userName)
        if  userName != name_of_user and required_length > 4:
            return True
        else:
            return False


    def validate_age (self,user_age):
        validated_age = type(int)
        # invalid_age = type(str)
        if validated_age and user_age > 0:
            return True
            
        else:
            return False

    def validate_gender(self,gender):
        if (gender == 'male') or (gender == 'female') or (gender == 'MALE') or (gender == 'FEMALE'):
            return True
        else:
            return False  

