import pyperclip, random, string
from credentials import Credentials
from user import User


def create_user_account(username,password):
    """function to create a user's account"""
    new_user = User(username,password)
    return new_user

def save_user(username,password):
    """saves a new user"""
    User.save_user(username,password)

def login(username,password):
    """"""
    User.login(username,password)

def create_credentials(account_name,account_username,account_password):
    """function to create new credentials"""
    new_credentials = Credentials(account_name,account_username,account_password)
    return new_credentials

def save_credentials(credentials):
    """funtion to save credentials"""
    credentials.save_creds()

def del_credentials(credentials):
    """function to delete credentials"""
    credentials.delete_creds()

def find_account(account):
    """function that searches for account"""
    return Credentials.search_by_account(account)

def account_existance(account):
    """function that checks wheather a certain account exists"""
    return Credentials.credential_exist(account)

def display_credentials():
    """function that displays credentials available"""
    return Credentials.display_credentials()

def copy_credentials(account):
    """function to copy a certain accounts credentials"""
    account_found = Credentials.search_by_account(account_found)
    pyperclip.copy(account_found.username)


def main():
    while True:
        print("Welcome to password locker")
        print("")
        print("Use the following short codes: cu - Create a new account, li - Login to your acount.")

        short_code = input().lower()
        if short_code == "cu":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            confirm_password = input("Confirm your password: ")
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
            while User.login(log_username,log_password):
                print("")
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
                    if pwd == 'gen':
                        length = int(input('How long do you want your password to be? '))
                        lower = string.ascii_lowercase
                        upper = string.ascii_uppercase
                        num = string.digits
                        symbols = string.punctuation

                        all = lower + upper + num + symbols
                        temp = random.sample(all,length)
                        account_password = "".join(temp)

                        save_credentials(create_credentials(account_name,account_username,account_password))

                    elif pwd == "man":
                        account_password = input("Enter your password: ")
                        save_credentials(create_credentials(account_name,account_username,account_password))

                elif option == "2":
                    #Search for credentials
                    account_to_find = input("Enter account name which you want to get the credentials: ")
                    if account_existance(account_to_find):
                        account = find_account(account_to_find)
                        print(f"Account: {account.account}")
                        print(f"Username: {account.username}")
                        print(f"Password: {account.password}")
                    else:
                        print("Account doesn't exists")
                
                elif option == "3":
                    #View credentials
                    if display_credentials():
                        print("Here is a list of all your credentials")
                        print("")
                        print("Acc.Name:    Username    Password ")
                        print("-"*50)
                        for creds in display_credentials():
                            print(f"{creds.account}   {creds.username}   {creds.password}")
                            print("")
                    else:
                        print("")
                        print("You have no credentials saved")
                        print("")
                
                elif option == "4":
                    #delete credentials
                    account_to_find = input("Enter account you want to delete: ")
                    if account_existance(account_to_find):
                        account = find_account(account_to_find)
                        print(f"{account.account}'s credentials will be deleted")
                        del_credentials(account)   
                        print("Account successfully deleted")
                    else:
                        print("Account doesnt exist")

                elif option == "5":
                    print("Bye.. \n see you later")
                    break                 



            else:
                print("Incorrect details please try again")
                break
                

                    
                    
                
                
        else:
            print("You must first create an account. use -cu-")
            # short_code == "li"
            # log_username = input("Enter your username: ")
            # log_password = input("Enter your password: ")
                
            # if User.login(log_username,log_password): 
            #     print("Select an option from below")
                    

main()