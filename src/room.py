# Implement a class to hold room information. This should have name and
# description attributes.

import os 
import time

# Room class 
class  Room:
    def __init__(self, name, description):
        self.name = name 
        self.description = description 
        self.items = [] # list to store items

        n_to, s_to, e_to, w_to = None, None, None, None 

        