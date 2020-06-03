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
    def __init__(self,name=Input(str), greet):
        self.name = name 
        self.greet = greet 

        name = Input("Name yourself or meet my Holy Sword, Rickerd.\n")
        print("Ah, " + name + ".")
        print("You have entered my chasm of rooms. For glory I presume.. matters not.\n")
        print("All who enter my chasm perish. On with it, be on your way.\n")

        
