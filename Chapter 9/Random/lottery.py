import random
import string

'''Emulates having a ticket and analyses how many times to win.'''
lottery = []
my_ticket = [12, 'h', 19, 15]
results = []
counter = 0

'''Damn I made it too good that it's statistically too difficult to find the answer'''
while counter < 1000: #1000 is placeholder to not practically make an infinite.
    lottery.clear()
    results.clear()

    for x in range(10):
            lottery.append(random.randint(1, 99))
            random.shuffle(lottery)
    for x in range(5):
        lottery.append(random.choice(string.ascii_lowercase))
        random.shuffle(lottery)
    for x in range(4):
        results.append(random.choice(lottery))
    for x in range(len(results)):
        results[x] = str(results[x])
        my_ticket[x] = str(my_ticket[x])
    print(f'The following ticket holder of: {results} wins!')

    if sorted(my_ticket) != sorted(results):
        counter += 1
        print(f'Unlucky! you\'ve now tried {counter} times. Try again!')
    else:
        print(f'Wow it only took {counter} tries!')
        print(f'The winning ticket is {lottery} and your ticket is {my_ticket}')
        break
