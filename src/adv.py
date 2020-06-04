# class imports 
from room import Room
from player import Player 
from item import Item 

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
player = Player('test player', room['outside'])
room['outside'].items = [item['A Sack Of Potatoes'], item['Iskanders Journal']]
room['treasure'].items = [item['Broken Clock']]
room['overlook'].items = [item['Blunt Axe'], item['Hegels Dialectic']]



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
start = 'Starting Game. . .'
while start[0] != 'q':

    print(f"Current room:{player.current_room.name} \
            \n{player.current_room.description} \
            \nitems in room: {', '.join([item.name for item in player.current_room.items])}")
    print("\nChoose Your path, or don't or whatevuh.")
    # Guide for player 
    print(f""" Your inventory: {len(player.items)}   Perform an action: Take, Grab, Walk, die.
                            
                            Map
                    --------------------
                             n
                          w     e
                             s             """)
    start = input("~~~~~~~~~~~: ")
    # Parse response into verbs and nouns. Beyond two inputs are ignored
    verb_noun = ['verb','noun']
    resp_list = start.split()
    verb_noun_dict = dict(zip(verb_noun,resp_list))
    verb, noun = verb_noun_dict.get('verb', False), verb_noun_dict.get('noun', False)
    try:
        if noun: # Check if 2nd argument is made, if so, assume it's a noun
            if verb == 'take':
                player.gain_item(item.get(noun, False)) # return False if not exist
            elif verb == 'drop':
                player.lose_item(item.get(noun, False))
            else:
                raise AttributeError
        else: # If eval fails, exec will not change
            next_room = eval(f'player.current_room.{verb}_to')
            if next_room != None:
                exec(f'player.current_room = player.current_room.{verb}_to')
                os.system('clear')
            else:
                os.system('clear')
                print("Are you shtupid? Innit clear that that tis the wrong way.")
                time.sleep(1)
    except AttributeError:
        if start[0] == 'q':
            print("You can't escape, only death will release you, meet my Holy Sword. ")
        elif start[0] == 'i':
            os.system('clear')
            player.show_inventory()
            time.sleep(1)
        else:
            os.system('clear')
            print(f'invalid option, "{start}" not understood, try again...')
            time.sleep(1)