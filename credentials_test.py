from credentials import Credentials
import unittest
import pyperclip

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
        self.new_credentials.save_creds()
        self.new_credentials.delete_creds()

        self.assertEqual(len(Credentials.credential_list),0)

    def test_search_by_account(self):
        """
        test to check if we can find account credentials by account name and display information
        """
        self.new_credentials.save_creds()
        account_found = Credentials.search_by_account("Instagram")
        
        self.assertEqual(account_found.username,self.new_credentials.username)

    def test_credential_exist(self):
        """
        test to check if we can return a Boolean if we cannot find the account
        """
        self.new_credentials.save_creds()
        account_found = Credentials.search_by_account("Instagram")

        self.assertTrue(account_found)      

    def test_display_credentials(self):
        """method that returns a list of all contacts saved
        """

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    def test_copy_credentials(self):
        """
        """
        self.new_credentials.save_creds()
        Credentials.copy_credentials("Instagram")

        self.assertEqual(self.new_credentials.username,pyperclip.paste())



if __name__=="__main__":
    unittest.main()