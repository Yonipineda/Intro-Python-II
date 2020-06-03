# class imports 
from room import Room
from player import Player 
from item import Item 
from greet import Greetings

# Basic imports 
import os 
import time 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



# Items 
item = {
    'A Sack Of Potatoes' : Item('A Sack Of Potatoes', '''HAHAHA, fool. 
            Those are no mere potatoes. They come from soil gifted from the gods. It is said, 
            by a man I meet some time ago, that should you consume them, you will be stripped
            from hunger. No longer shall human necessity chain you.'''),

    '$3.50' : Item('$3.50', '''Spare change, always a plus! Too bad you won't escape nor 
                    live to ever have need for such worldly things.'''),

    'Hegels Dialectic' : Item('Hegels Dialectic', '''Hm.'''),

    'Blunt Axe' : Item('Blunt Axe', '''An Axe tested in battle. War Ready, don't judge it for 
                        its scar's but for its earned glory.'''),

    'Broken Clock' : Item('Broken Clock' , '''A relic of an age long gone.'''), 

    'Iskanders Journal' : Item('Iskanders Journal', '''Notes left unfinished and pages burnt.
                                There seems to be a name, Iskanders? Hm, I don't recall such 
                                a man.''')



}

# Player 
player = Player('player', room['outside'])
room['outside'].items = [item[ot] for ot in str(Item)] 
room['treasure'].items = [item[t] for t in str(Item)]
room['overlook'].items = [item[o] for o in str(Item)]
room['foyer'].items = [item[f] for f in str(Item)] 
room['narrow'].items = [item[n] for n in str(Item)]



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# Start The Game! 
start = Greetings(name=Input("Name yourself or meet my Holy Sword, Rickerd.\n")
while start[0] != None:
    '''An introduction'''

        # Tomchomp, Wielder of Rickard, Greets the player.
        print("Ah, " + name + ".")
        print("You have entered my chasm of rooms. For glory I presume.. matters not.\n")
        print("All who enter my chasm perish. On with it, be on your way.\n")

        # Player now chooses a path 
        print(f"Now, {name}, choose a path to traverse, have no regrets.")