from user import User
from authexception import UsernameAlreadyExists,PasswordTooshort

class authentificator:
    def __init__(self):

        self.user={}
    def add_user(self,user_name,password):
            
        if user_name in self.users:
            raise UsernameAlreadyExists(user_name)
        if len(password) < 4:
            raise PasswordTooshort(user_name)
        self.user[user_name]=User(user_name,password)

        

        pass