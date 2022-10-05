"""Import the random module"""
import random

"""A random head or tail generator using the random module"""
random_number = random.random()
if random_number <=0.5:
    print(random_number)
    print('you chose head')
else:
    print(random_number)

    print('you picked tail')

