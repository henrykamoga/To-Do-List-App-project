
import unittest

from validation import Register_user


email1 = "jacob2016henry@gmail.com"
email2 = "jacob2016henry@gmail"
email3 = "jacob2016henry"
password = "HeN0@1"

class Test_all_validations (unittest.TestCase):
    

    def setUp(self):
        self.register =  Register_user(email1,password)
        print ("")

    def test_instance_of_register(self):
        self.assertIsInstance(self.register,Register_user)

    def test_email_validation(self):
        self.assertTrue(self.register.validate_email(email1))
        self.assertFalse(self.register.validate_email(email2))
        self.assertFalse(self.register.validate_email(email3))
