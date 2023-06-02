import random

from player import Player

class AiPlayer(Player):
    def __init__(self, choices):
        super().__init__(self)
        self.ai_play = random.choice(choices)
            