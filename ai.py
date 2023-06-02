import random

from player import Player

class AiPlayer(Player):
    def __init__(self):
        super().__init__(self)
        gesture_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        ai_choices = random.choice(gesture_choices)
            