from user import User
import unittest

class TestUser(unittest.TestCase):
    """
    Test Class that tests methods present in our Userclass
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """setup method to run before all other test casses"""
        self.new_user = User("Benson","vcxz4321")
    
    def tearDown(self):
        """tearDown method that does clean up after each test case has run"""
        User.users = {}

    def test_init(self):
        """ test_init testcase to test if the object is initialized properly"""
        self.assertEqual(self.new_user.username,"Benson")
        self.assertEqual(self.new_user.password,"vcxz4321")
    
    def test_save_user(self):
        """test_user_save will test wheather our new user gets added to the dictionary"""
        User.save_user(self.new_user.username,self.new_user.password)
        self.assertEqual(len(User.users),1)
    
    def test_login(self):
        """test_login will test whether an existing user can login"""
        User.save_user(self.new_user.username,self.new_user.password)
        self.assertTrue(User.login(self.new_user.username,self.new_user.password))

if __name__=="__main__":
    unittest.main()
    

