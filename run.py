import pyperclip, random
from credentials import Credentials
from user import User



print("Welcome to PassWord Locker")

def create_credentials(account_name,account_username,account_password):
    """function to create new credentials"""
    new_credentials = Credentials(account_name,account_username,account_password)

def save_credentials(credentials):
    """funtion to save credentials"""
    Credentials.credential_list.append(credentials)

def del_credentials(credentials):
    """function to delete credentials"""
    Credentials.credential_list.remove(credentials)

def find_account(account):
    """function that searches for account"""
    Contact.search_by_account(account)

def account_existance(account):
    """function that checks wheather a certain account exists"""
    Contact.credential_exist(account)

def copy_credentials(account):
    """function to copy a certain accounts credentials"""
    Contact.copy_credentials(account)