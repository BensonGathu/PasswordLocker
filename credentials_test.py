from credentials import Credentals
import unittest

class TestCredentials(unittest.TestCase):
    """
    Test Class that tests methods present in the Credentials Class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """the setUp method to runbefore all other test casses"""
        self.new_credentials = Credentals("Instagram","bensongathu","vcxz4321")
    
    def tearDown(self):
        """tearDown method that does clean up after each test case has run"""
        pass
    
    