import hashlib
class User:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.status=False
        self.password=self._encrypt_password(password)

    def check_password (self,password) -> bool:
        encrypted_password = self._encrypt_password(password)
        return encrypted_password == self.password

    def _encrypt_password(self,password) ->str:
        """
        crype le mot de passe en utilisant l'algorithme SHA-256

        Args:
            password (_type_): _description_

        Returns:
            str: _description_
        """

        
        password_encoded = password.encode('utf-8')
        return hashlib.sha256(password_encoded).hexdigest()
user = User('john','password')
print(user.check_password('password'))
    
     
