
import unittest

from validation import Register_user

name1 = 'henry'
name2 = 2

email1 = "jacob2016henry@gmail.com"
email2 = "jacob2016henry@gmail"
email3 = "jacob2016henry"

password1 = "Henry1@"
password2 = "henry1"
password3 = "hen"

name_of_user = "henry"
username1 = "jacob"
username2 = "jac"
username3 = "henry"

age1 = 8
age2 = "two"

gender1 = 'male' 
gender2 = 'female'
gender3 = 'MALE' 
gender4 = 'FEMALE'
gender5 ='man'


class Test_all_validations (unittest.TestCase):
    

    def setUp(self):
        self.register =  Register_user(name1,email1,password1,username1,age1,gender1)
        print ("")

    def test_instance_of_register(self):
        self.assertIsInstance(self.register,Register_user)

    def test_name_validation(self):
        self.assertTrue(self.register.validate_name(name1))
        self.assertTrue(self.register.validate_name(name2))


    def test_email_validation(self):
        self.assertTrue(self.register.validate_email(email1))
        self.assertFalse(self.register.validate_email(email2))
        self.assertFalse(self.register.validate_email(email3))


    def test_password_validation(self):
        self.assertTrue(self.register.validate_password(password1))
        self.assertFalse(self.register.validate_password(password2))
        self.assertFalse(self.register.validate_password(password3))

    def test_username_validation(self):
        self.assertTrue(self.register.validate_username( name_of_user,username1))
        self.assertFalse(self.register.validate_username(name_of_user,username2))
        self.assertFalse(self.register.validate_username(name_of_user,username3))

    def test_age_validation(self):
        self.assertTrue(self.register.validate_age(age1))
        # self.assertFalse(self.register.validate_age(age2))

    def test_gender_validation (self):
        self.assertTrue(self.register.validate_gender(gender1))
        self.assertTrue(self.register.validate_gender(gender2))
        self.assertTrue(self.register.validate_gender(gender3))
        self.assertTrue(self.register.validate_gender(gender4))
        self.assertFalse(self.register.validate_gender(gender5))
        


    def tearDown (self):
        print ("____testing done____")
        print ("")


if __name__=='__main__':
    unittest.main()
