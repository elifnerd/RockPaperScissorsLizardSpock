#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

from ai import AiPlayer

def prompt_player():
    user_input = input('Welcome, Player. Have you played this game before? Y/N')
    time.sleep(2)
    if user_input == 'Y':
        print('Great. Welcome back! Lets get started.')
    elif user_input == 'N':
        print('Great. This is much like your classic game of Rock, Paper, Scissors - with a little twist. In the classic game, Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock. Those rules still apply with some additional options. Rock also crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, and Spock vaporizes Rock. Lets get started.')
    else:
        print('Im sorry. I didnt understand. Have you played this game before? Please choose Y or N.')
            
def run_game():
     players = input('How many players? 1 or 2?')
     time.sleep(2)
     if players == '1':
         print('Wonderful. Your options are as follows.')
         time.sleep(1)
         print('Choose 1 for Rock')
         time.sleep(1)
         print('Choose 2 for Paper')
         time.sleep(1)
         print('Choose 3 for Scissors')
         time.sleep(1)
         print('Choose 4 for Lizard')
         time.sleep(1)
         print('Choose 5 for Spock')
     elif players == '2':
         pass
     
def first_round():
    round_one_gesture = input('Please make your selection.')
    time.sleep(1)
    if round_one_gesture == '1':
        print('You have chosen Rock.')
    