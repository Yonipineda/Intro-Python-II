import os 
import sys 
import time 
from room import Room 

'''
build a story 
'''

choice = ['yes', 'no']

class Greetings:
    '''Greet the player'''
    def __init__(self, name=Input(str)):
        self.name = name 

    def __str__(self):
        return self.name
       

        


