import random

class Die:
    #A die to play with.#

    def __init__(self):
        self.value = random.randint(1, 6)

        print (self.value)


    def roll(self):
        #Returns the rolled dice, or raises RolledOneException if 1.#

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RolledOneException

        print (self.value)


    def __str__(self):
        print ("Rolled " + str(self.value) + ".")