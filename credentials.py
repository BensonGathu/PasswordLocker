import pyperclip

class Credentals:
    #class that generates new instances of credentials
    credential_list = []
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

    def save_creds(self):
        """method that saves created credentials"""
        Credentals.credential_list.append(self)
    
    def delete_creds(self)
        """method that deletes credentials from our credentials list"""
        Credentals.credential_list.remove(self)

    @classmethod
    def search_by_account(cls,account):
        """
        method that takes in an account name and returns a account username and password that matches that account name.
        Args:
            account: Account name  to search for.
        REturns:
            Details of account  that matches the name.
        """
        for credentials in cls.credential_list:
            if credentials.account == account:
                return credentials

    @classmethod
    def credential_exist(cls,account):
          """
        method that checks if an account exists from the credentials_list. 
        Args:
            account: Account name to search if it exists
        Returns:
            Boolean: True or false depending if the credentials exists
        """
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
            return False

    @classmethod
    def display_credentials(cls):
        """method that returns all my existing credentials"""
        return cls.credential_list
    
    @classmethod
    def copy_credentials(cls,account):
        """method that will copy an accounts credentials"""
        account_found = search_by_account(account)
        pyperclip.copy(account_found.username,account_found.password)