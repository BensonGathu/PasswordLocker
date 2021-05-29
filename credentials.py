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

    