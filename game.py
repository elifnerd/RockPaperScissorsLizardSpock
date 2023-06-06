#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

import random

from ai import AiPlayer

def winner_winner(player_one_choice, player_two_choice):
    if player_one_choice == player_two_choice:
        return 'tie'
    elif player_one_choice == '1':
        if player_two_choice == '3' or player_two_choice == '4':
            return 'Player One wins!'
        else:
            return 'Player Two wins'
    elif player_one_choice == '2':
        if player_two_choice == '1' or player_two_choice == '5':
            return 'Player One wins!'
        else:
            return 'Player Two wins!'
    elif player_one_choice == '3':
        if player_two_choice == '2' or player_two_choice == '4':
            return 'Player One wins!'
        else:
            return 'Player Two wins!'
    elif player_one_choice == '4':
        if player_two_choice == '2' or player_two_choice == '5':
            return 'Player One wins!'
        else:
            return 'Player Two wins!'
    elif player_one_choice == '5':
        if ai_choice == 'Scissors' or ai_choice == 'Rock':
            return 'Player One wins!'
        else:
            return 'Player Two wins!'
        
def play_game():
    player_one_score = 0
    player_two_score = 0
    
        
def display_gameplay_rules():
    print('This is much like your classic game of Rock, Paper, Scissors - with a little twist.')
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
    print('The winner will be the best out of three.')

def single_player_mode():
    player_score = 0
    ai_score = 0
    round_count = 0
    
    while player_score < 2 and ai_score < 2:
        print('Please make your selection: ')
        time.sleep(1)
        print('Select 1 for Rock')
        time.sleep(1)
        print('Select 2 for Paper')
        time.sleep(1)
        print('Select 3 for Scissors')
        time.sleep(1)
        print('Select 4 for Lizard')
        time.sleep(1)
        print('Select 5 for Spock')
        
        player_choice = input('Your move: ')
        gesture_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        player_choice = gesture_choices[int(player_choice) - 1]
        ai_choice = random.choice(gesture_choices)

    print('You have chosen', player_choice)
    print('AI has chosen', ai_choice)
    round_count += 1

    round_winner = winner_winner(player_choice, ai_choice)
    
    if round_winner == 'tie':
        print('Its a tie!')
    elif round_winner == 'Player One':
        print('Player One wins this round.')
        player_one_score += 1
    else:
        print('AI wins this round.')
        ai_score += 1
        print('Player Ones score is', player_score)
        time.sleep(1)
        print('AIs score is', ai_score)
        print()
        
        if player_score > ai_score:
            print('Congratulations, Player One! You have won the game.')
        else:
            print('Boo, AI has won the game. Better luck next time.')
        
        
    
def multiplayer_mode():
    player_one_score = 0
    player_two_score = 0
    round_count = 0
    
    while player_one_score < 2 and player_two_score < 2:
        round_count += 1
        print('Round', round_count, 'Lets go again.')
    
    player_one_choice = input('Player One, please make your selection...')

    print('Player One has chosen', player_one_choice)
    time.sleep(1)
        
    player_two_choice = input('Player Two, please make your selection...')
    
    print('Player Two has chosen', player_two_choice)
    time.sleep(1)
    
    winner = winner_winner(player_one_choice, player_two_choice)
    if winner == 'tie':
        print('Its a tie!')
    elif winner == 'Player One':
        print('Player One wins this round.')
        player_one_score += 1
    else:
        print('Player Two wins this round.')
        player_two_score += 1
        
    print ('Player Ones score is', player_one_score)
    print('Player Twos score is', player_two_score)
    
    if player_one_score > player_two_score:
        print('Congratulations, Player One! You have won the game.')
    else:
        print('Congratulations, Player Two! You have won the game.')


def prompt_player():
    user_input = input('Welcome, player(s)! How many players do we have today? Select 1 or 2...')
    if user_input == '1':
        print('Fantastic. You will be playing against our AI program today. Lets get started.')
        return display_gameplay_rules()
        return single_player_mode()
    elif user_input == '2':
        print('Fantastic. Your names will be Player One and Player Two. Lets get started.')
        return display_gameplay_rules()
        return multiplayer_mode()
    else:
        print('I am sorry. I did not understand. Lets try again.')
        return user_input
    