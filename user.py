class User:
    """class for creating new instances of users"""
    users = {}
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod
    def save_user(cls,username,password):
        """method that saves a created user"""
        cls.users[username] = password

    @classmethod
    def login(cls,username,password):
        """ """
        if username in cls.users and password == cls.users[username]:
            return True
        return False
 