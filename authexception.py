class AuthException(Exception):
    def __init__(self,user_name,user=None ):
        self.user_name=user_name
        super().__init__(self,user_name,user)
        self.user_name=user_name
        self.user=user
class UsernameAlreadyExists(AuthException):
    pass
class PasswordTooshort(AuthException):
    pass
class invalidUserName(AuthException):
    pass
class invalidpassword(AuthException):
    pass
class NoPermission(AuthException):
    pass