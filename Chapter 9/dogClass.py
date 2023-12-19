# Write your code here :-)
class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f'{self.name} is now sitting.')

    def rollOver(self):
        '''Simulate a dog rolling over'''
        print(f'{self.name} is now rolling over.')

myDog = Dog('Willie', 6)
print(f'My dog\'s name is {myDog.name}.')
myDog.sit()
myDog.rollOver()
