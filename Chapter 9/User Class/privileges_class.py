from userClass import User

class Privileges(User):
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'Privileges are: {privilege}')
