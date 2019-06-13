import random

class Player:
    
    def __init__(self, name=None):
        self.name = name
        self.score = 0

    def add_score(self, player_score):
        self.score += player_score

    # def __str__(self):
    #     return str(self.name) + ": " + str(self.score)

class Dice:
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        self.value = random.randint(1, 6)

    # @staticmethod # look up
    # def rolled_one():
    #     print("Rolled 1. \n")

    # def __str__(self):
    #     return "Rolled " + str(self.value) + "."


class ComputerPlayer(Player):
    cpu_names=['Lisa','Daniel', 'Christina']

    def __init__(self, number):
       
        # if number < len(self.cpu_names):
        #     name = self.cpu_names[number]
        # else:
        #     name = 'Cpu{}'.format(number)

        super(ComputerPlayer, self).__init__(name)

    def keep_rolling(self, ?):

class HumanPlayer(Player):
    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)


    def keep_rolling(self, box):
        """Asks the human player, if they want to keep rolling."""

        human_decision = input_number("  1 - Roll again, 0 - Hold? ", 0, 1)
        if human_decision == 1:
            return True
        else:
            return Falses
        
class Score:()
pass

class Gameloop()
pass



player_one_score = []
computer_player = []

class_die = Dice
class_die(self.value)
