#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

from ai import AiPlayer

def winner_winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return 'Its a tie! Go again.'
    elif player_choice == '1':
        if ai_choice == 'Scissors' or 'Lizard':
            return 'Player One wins the round.'
        else:
            return 'AI wins the round.'
    elif player_choice == '2':
        if ai_choice == 'Rock' or 'Spock':
            return 'Player One wins the round.'
        else:
            return 'AI wins the round.'
    elif player_choice == '3':
        if ai_choice == 'Paper' or 'Lizard':
            return 'Player One wins the round.'
        else:
            return 'AI wins the round.'
    elif player_choice == '4':
        if ai_choice == 'Spock' or 'Paper':
            return 'Player One wins the round.'
        else:
            return 'AI wins the round.'
    elif player_choice == '5':
        if ai_choice == 'Scissors' or 'Rock':
            return 'Player One wins the round'
        else:
            return 'AI wins the round.'

def prompt_player():
    user_input = input('Welcome, Player. Have you played this game before? Y/N')
    time.sleep(1)
    if user_input == 'Y':
        print('Great. Welcome back! Lets get started.')
        time.sleep(1)
        print('Your selections are as follows:')
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
        print('Your selections are as follows:')
    else:
        return 'Im sorry. I didnt understand.'
    while user_input != 'Y' or 'N':
        return prompt_player()
        
def single_player():
    player_score = 0
    ai_score = 0
    round_count = 0
    
    while player_score < 2 and ai_score < 2:
        round_count += 1
        print('Round', round_count, 'Lets go again.')
        
        
    player_choice = input('Please make your selection...')
    if player_choice == '1':
        return 'You have chosen Rock.'
    elif player_choice == '2':
        return 'You have chosen Paper.'
    elif player_choice == '3':
        return 'You have chosen Scissors.'
    elif player_choice == '4':
        return 'You have chosen Lizard.'
    elif player_choice == '5':
        return 'You have chosen Spock.'
    else:
        return 'I am sorry. I did not understand. Lets try again.'
        time.sleep(1)
        player_choice()
    ai_choice = AiPlayer().gesture_choices
    if player_choice == ai_choice:
        return 'Its a tie! Lets go again.'
    else:
        return player_choice()
        
    
def multiplayer():
    player_one_score = 0
    player_two_score = 0
    round_count = 0
    
    while player_one_score < 2 and player_two_score < 2:
        round_count += 1
        print('Round', round_count, 'Lets go again.')
    
    player_one_choice = input('Player One, please make your selection...')
    if player_one_choice == '1':
        return 'You have chosen Rock.'
    elif player_one_choice == '2':
        return 'You have chosen Paper.'
    elif player_one_choice == '3':
        return 'You have chosen Scissors.'
    elif player_one_choice == '4':
        return 'You have chosen Lizard.'
    elif player_one_choice == '5':
        return 'You have chosen Spock.'
    else:
        return 'I am sorry. I did not understand. Lets try again.'
        time.sleep(1)
        return player_one_choice()
        
    player_two_choice = input('Player Two, please make your selection...')
    if player_two_choice == '1':
        return 'You have chosen Rock.'
    elif player_two_choice == '2':
        return 'You have chosen Paper.'
    elif player_two_choice == '3':
        return 'You have chosen Scissors.'
    elif player_two_choice == '4':
        return 'You have chosen Lizard.'
    elif player_two_choice == '5':
        return 'You have chosen Spock.'
    else:
        return 'I am sorry. I did not understand. Lets try again.'
        time.sleep(1)
    if player_one_choice == player_two_choice:
        print('Its a tie! Lets go again.')
    else:
        return player_two_choice()

            
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