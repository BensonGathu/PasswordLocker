import pyperclip, random
from credentials import Credentials
from user import User


def create_user_account(username,password):
    """function to create a user's account"""
    new_user = User(username,password)

def save_user():
    """saves a new user"""


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

def display_credentials():
    """function that displays credentials available"""

def copy_credentials(account):
    """function to copy a certain accounts credentials"""
    Contact.copy_credentials(account)



def main():
    while True:
        print("Welcome to password locker")
        print("")
        print("Use the following short codes: cc - Create a new account, li - Login to your acount.")


    
main()