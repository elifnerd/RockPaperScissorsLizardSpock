#Display welcome -- Write a function that welcomes the player
#Explain rules of the game -- Write a funct that explains
#Create a user input funct for game players(will have option for unsatisfactory user input)
import time

import random

from ai import AiPlayer

def winner_winner(player_one_choice, player_two_choice):
    if player_one_choice == player_two_choice:
        return 'tie'
    elif player_one_choice == 'Rock':
        if player_two_choice == 'Scissors' or player_two_choice == 'Lizard':
            return 'Player One'
        else:
            return 'Player Two'
    elif player_one_choice == 'Paper':
        if player_two_choice == 'Rock' or player_two_choice == 'Spock':
            return 'Player One'
        else:
            return 'Player Two'
    elif player_one_choice == 'Scissors':
        if player_two_choice == 'Paper' or player_two_choice == 'Lizard':
            return 'Player One wins'
        else:
            return 'Player Two wins'
    elif player_one_choice == 'Lizard':
        if player_two_choice == 'Paper' or player_two_choice == 'Spock':
            return 'Player One'
        else:
            return 'Player Two'
    elif player_one_choice == 'Spock':
        if player_two_choice == 'Scissors' or player_two_choice == 'Rock':
            return 'Player One'
        else:
            return 'Player Two'
    
        
def welcome_and_display_gameplay_rules():
    print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
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
    
    while player_score < 2 and ai_score < 2:
        print('Select 1 for Rock...')
        time.sleep(1)
        print('Select 2 for Paper...')
        time.sleep(1)
        print('Select 3 for Scissors...')
        time.sleep(1)
        print('Select 4 for Lizard...')
        time.sleep(1)
        print('Select 5 for Spock...')
        time.sleep(1)
        player_choice = input('Your move: ')
        gesture_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        player_choice = gesture_choices[int(player_choice) - 1]
        ai_choice = random.choice(gesture_choices)
        print('You have chosen ', player_choice)
        print('Sheldon has chosen ', ai_choice)
        round_winner = winner_winner(player_choice, ai_choice)
        if round_winner == 'tie':
            print('Its a tie!')
        elif round_winner == 'Player One':
            print('Player One wins this round.')
            player_score += 1
        else:
            print('Sheldon wins this round.')
            ai_score += 1
            print('Your score is ', player_score)
            time.sleep(1)
            print('Sheldons score is ', ai_score)
            print()
        
    if player_score > ai_score:
        print('Congratulations! You have won the game.')
    else:
        print('Boo, Sheldon has won the game. Better luck next time.')
        
        
    
def multiplayer_mode():
    player_one_score = 0
    player_two_score = 0
    
    while player_one_score < 2 and player_two_score < 2:
        print('Select 1 for Rock...')
        time.sleep(1)
        print('Select 2 for Paper...')
        time.sleep(1)
        print('Select 3 for Scissors...')
        time.sleep(1)
        print('Select 4 for Lizard...')
        time.sleep(1)
        print('Select 5 for Spock...')
        time.sleep(1)
        gesture_choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        player_one_choice = input('Player One, please make your selection...')
        time.sleep(1)
        if player_one_choice == "1" or player_one_choice == '2' or player_one_choice == '3' or player_one_choice == '4' or player_one_choice == '5':
            pass
        else: 
            print('I am sorry. I did not understand. Lets try again.')
            return player_one_choice
        player_one_move = gesture_choices[int(player_one_choice) - 1]
        player_two_choice = input('Player Two, please make your selection...')
        time.sleep(1)
        if player_two_choice == "1" or player_two_choice == '2' or player_two_choice == '3' or player_two_choice == '4' or player_two_choice == '5':
            pass
        else: 
            print('I am sorry. I did not understand. Lets try again.')
            return player_two_choice
        player_two_move = gesture_choices[int(player_two_choice) - 1]
        print('Player One has chosen', player_one_move)
        time.sleep(1)
        print('Player Two has chosen', player_two_move)
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
    user_input = input('How many players do we have today? Select 1 or 2...')
    if user_input == '1':
        print('Fantastic. You will be playing against our AI program, aka Sheldon, today. Lets get started.')
        return single_player_mode()
    elif user_input == '2':
        print('Fantastic. Your names will be Player One and Player Two. Lets get started.')
        return multiplayer_mode()
    else:
        print('I am sorry. I did not understand. Lets try again.')
        return prompt_player()
    