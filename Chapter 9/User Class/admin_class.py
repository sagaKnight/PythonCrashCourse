# Write your code here :-)
from userClass import User
from privileges_class import Privileges

class Admin(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
