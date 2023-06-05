#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

import random

from ai import AiPlayer

def winner_winner(player_one_choice, player_two_choice):
    if player_one_choice == player_two_choice:
        return 'Its a tie! Go again.'
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

def prompt_player():
    user_input = input('Welcome, Player. Have you played this game before? Y/N')
    if user_input == 'Y':
        print('Great. Welcome back! Lets get started.')
    elif user_input == 'N':
        print(display_gameplay_rules())
    else:
        return 'Im sorry. I didnt understand.'
        user_input()
        
def single_player():
    player_score = 0
    ai_score = 0
    round_count = 0
    
    while player_score < 2 and ai_score < 2:
        round_count += 1
        print('Round', round_count, 'Lets go again.')
        
    gesture_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']    
    player_choice = input('Please make your selection...')
    ai_choice = random.choice(gesture_choices)

    print('You have chosen', player_choice)
    print('AI has chosen', ai_choice)

    winner = winner_winner(player_choice, ai_choice)
    
    if winner == 'tie':
        print('Its a tie!')
    elif winner == 'Player One':
        print('Player One wins this round.')
        player_score += 1
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
        
        
    
def multiplayer():
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
