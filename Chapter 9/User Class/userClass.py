# Write your code here :-)
class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0

    def describe_user(self):
        print(f'The first name is {self.fname} and the last name {self.lname}')

    def greet_user(self):
        print(f'Hello {self.fname} {self.lname}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


