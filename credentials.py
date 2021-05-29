import pyperclip

class Credentals:
    #class that generates new instances of credentials
    credentials = []
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

    def save_creds(self):
        """method that saves created credentials"""