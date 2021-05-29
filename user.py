class User:
    """A class for creating users"""
    users = {}
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):
        """method that saves a created user"""
        User.users[self.username] = self.password

    @classmethod
    def login(cls,username):
        pass
