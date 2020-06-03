# Write a class to hold player information, e.g. what room they are in
# currently.

import os 
import time 

# Player class 
class Player:
    def __init__(self, name, current_room):  # name of player and his current room
        self.name = name 
        self.current_room = current_room 
        self.items = [] # empty list to store items 

        name: str 
        current_room: str 

    def curr_items(self): 
        '''Items player has taken'''
        if len(self.items) == 0:
            print("Player has no items or Player lives without material.")  # no items
        else:
            print("Players Item")  # does have items 
        for item in self.items:
            print("{}: {}\n".format(item, self.description)) # describe the item and its content

    def add_items(self, item):
        ''' Add/Gain items. removes from room'''
        os.system('clear') 
        if item:
            self.current_room.items.remove(item) # logic for add items 
            self.items.append(item)
            print("Added {} to inventory".format(item))
            print(item.description) 
            time.sleep(1) # wait a sec
        else:
            print("No such {} in this room.".format(item))
            time.sleep(1) # wait a sec


    def minus_item(self, item):
        '''Lose or remove item. adds back to room'''
        os.system('clear')
        try:
            self.items.remove(item) # delete item from inventory 
            self.current_room.items.append(item) # leave it in the room
            print("{} dropped in this shabby {}\n".format(item.name, self.current_room.name))



    