#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

from ai import AiPlayer

def prompt_player():
    user_input = input('Welcome, Player. Have you played this game before? Y/N')
    time.sleep(1)
    if user_input == 'Y':
        print('Great. Welcome back! Lets get started.')
    elif user_input == 'N':
        print('Great. This is much like your classic game of Rock, Paper, Scissors - with a little twist.')
        time.sleep(1)
        print('In the classic game, Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock.')
        time.sleep(1)
        print('Those rules still apply with some additional options.')
        time.sleep(1)
        print('Rock also crushes Lizard,')
        time.sleep(1)
        print('Lizard poisons Spock,')
        time.sleep(1)
        print('Spock smashes Scissors,')
        time.sleep(1)
        print('Scissors decapitates Lizard,')
        time.sleep(1)
        print('Lizard eats Paper,')
        time.sleep(1)
        print('Paper disproves Spock,')
        time.sleep(1)
        print('and Spock vaporizes Rock.')
        time.sleep(1)
        print('Lets get started.')
    else:
        print('Im sorry. I didnt understand. Have you played this game before? Please choose Y or N.')
        user_input
        
def single_player():
    player_choice = input('Please make your selection...')
    if player_choice == '1':
        print('You have chosen Rock.')
    elif player_choice == '2':
        print('You have chosen Paper.')
    elif player_choice == '3':
        print('You have chosen Scissors.')
    elif player_choice == '4':
        print('You have chosen Lizard.')
    elif player_choice == '5':
        print('You have chosen Spock.')
    else:
        print('I am sorry. I did not understand. Lets try again.')
        time.sleep(1)
        player_choice
    ai_choice = AiPlayer().gesture_choices
    if player_choice == ai_choice:
        print('Its a tie! Lets go again.')
        single_player()
        
    
def multiplayer():
    player_one_choice = input('Player One, please make your selection...')
    player_two_choice = input('Player Two, please make your selection.')
    if player_one_choice == player_two_choice:
        print('Its a tie! Lets go again.')
        multiplayer()
            
def run_game():
     players = input('How many players? 1 or 2?')
     time.sleep(1)
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
         single_player()
     elif players == '2':
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
         multiplayer()