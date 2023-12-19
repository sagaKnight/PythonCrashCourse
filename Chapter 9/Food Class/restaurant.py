# Write your code here :-)
class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.name}. The cuisine type is {self.cuisine}.')

    def open_restaurant(self):
        print(f'The restaurant {self.name} is now open!')

    def get_number_served(self):
        print(f'The restaurant has served {self.number_served}.')

    def set_number_served(self, new_val):
        self.number_served = new_val

    def increment_number_served(self):
        self.number_served += 1

class Ice_Cream_Stand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'mint choc chip']

    def get_flavors(self):
        for flavor in self.flavors:
            print(f'The Ice Cream Stand \'{self.name}\' has {flavor.title()}')
