# Write your code here :-)
''' A class which represents gas and electric cars.'''
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def getOdometerReading(self):
        '''Prints the mileage of the car'''
        print(f'The mileage of the car is {self.odometer}')

    def updateOdometer(self, mileage):
        '''Set the odometer reading to the given value.'''
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('The mileage can\'t be rolled back.')

    def incrementOdometer(self, miles):
        '''Adds the argument to the odometer'''
        self.odometer += miles

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def fill_gas_tank():
        print(f'Gas tank has been filled.')

class Battery:
    '''A simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    '''Represents aspects of a car, specialised to electric vehicles.'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)
        self.battery = Battery() # This line creates a new attribute to itself which is called battery. This initializes a new Battery Object.

    def fill_gas_tank(self):
        print(f'This car has no tank!')
