from .db import check_user_email
from passlib.hash import sha256_crypt
from datetime import datetime

class UserValidator:
    def __init__(self, name, email, password):
        self.name = name.strip()
        self.email = email.strip()
        self.password = password.strip()

        # we are going to validate the user
        try:
            self.valid = False
            if self.name != "":
                if self.email != "":
                    if check_user_email(self.email): # checking if it is an duplicate email or not
                        
                        if self.password != "":
                            self.valid = True
                            self.password = sha256_crypt.hash(self.password)
                            self.msg = "User Registered"
                        else:
                            self.msg = "Password is not valid"
                    else:
                        self.msg = "email is in use."
                else:
                    self.msg="email is not valid"
            else:
                self.msg="name can't be empty"
        except:
            self.valid = False
            self.msg="error occured, if this keep of showing contact developers."

    def data(self):
        return self.name, self.email, self.password, datetime.now()