from credentials import Credentials
import unittest

class TestCredentials(unittest.TestCase):
    """
    Test Class that tests methods present in the Credentials Class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """the setUp method to runbefore all other test casses"""
        self.new_credentials = Credentials("Instagram","bensongathu","vcxz4321")
    
    def tearDown(self):
        """tearDown method that does clean up after each test case has run"""
        Credentials.credential_list = []
    
    def test_init(self):
        """test_init testcase to test if the object is intialezed correctly"""
        self.assertEqual(self.new_credentials.account,"Instagram")
        self.assertEqual(self.new_credentials.username,"bensongathu")
        self.assertEqual(self.new_credentials.password,"vcxz4321")

    def test_save_creds(self):
        """test_save_creds will test wheather our credentials gets saved to our credentials list"""
        self.new_credentials.save_creds()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_delete_creds(self):
        """test_delete_creds testcase will check if we successfully deleter a credential from our credential_list"""
        self.    


if __name__=="__main__":
    unittest.main()