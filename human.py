from player import Player

class HumanPlayer(Player):
    def __init__(self, choices):
        super().__init__(choices)
        self.available_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']