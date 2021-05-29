import pyperclip, random, string
from credentials import Credentials
from user import User


def create_user_account(username,password):
    """function to create a user's account"""
    new_user = User(username,password)

def save_user(username,password):
    """saves a new user"""
    User.save_user(username,password)

def login(username,password):
    """"""
    User.login(username,password)

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
        print("Use the following short codes: cu - Create a new account, li - Login to your acount.")

        short_code = input().lower()
        if short_code == "cu":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            confirm_password = input("Re-enter your password: ")
            while password != confirm_password:
                confirm_password = input("Password do not match please enter again: ")
            else:
                create_user_account(username,password)
                save_user(username,password)
                print(f"Congratulations {username} account created successfully")

            print("")
            print("You can now login")
            print("")
            log_username = input("Enter your username: ")
            log_password = input("Enter your password: ")
            if User.login(log_username,log_password):
                print(f"Welcome: {log_username} to your Account") 
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print("_"*50)
                print("1: Add new credentials")
                print("2: Search credentials")
                print("3: View your credentials")
                print("4: Delete credentials")
                print("5: Log Out")
                option = input()

                if option == "1":
                    #adding new credentials
                    account_name = input("Account Name: ")
                    account_username = input("Username: ")
                    pwd = input("type 'gen' to generate password or 'man' to input your own password: ")
                    if pwd = 'gen':
                        length = int(input('How long do you want your password to be? '))
                        lower = string.ascii_lowercase
                        upper = string.ascii_uppercase
                        num = string.digits
                        symbols = string.punctuation

                        all = lower + upper + num + symbols
                        temp = random.sample(all,length)
                        account_password = "".join(temp)

                        save_credentials(create_credentials(account_name,account_username,account_password))

                    elif pwd = "man":
                        account_password = input("Enter your password: ")
                        save_credentials(create_credentials(account_name,account_username,account_password))
                        
                elif option == "2":


            else:
                print("Incorrect details provided")
                

                    
                    
                
                
        elif short_code == "li":
            log_username = input("Enter your username: ")
            log_password = input("Enter your password: ")
                
            if User.login(log_username,log_password): 
                print("Select an option from below")
                    



    
main()