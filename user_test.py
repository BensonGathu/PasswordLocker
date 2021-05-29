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
        pass


        
if __name__=="__main__":
    unittest.main()
    

