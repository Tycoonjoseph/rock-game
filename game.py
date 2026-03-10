import random 
options =['rock', 'paper', 'scissors']

def game(user_input, computer_input):
    if user_input == computer_input:
        return 'Its a tie!'
    elif user_input =='rock' and computer_input == 'scissors':
        return 'You win!'
    elif user_input == 'paper' and computer_input == 'rock':
        return 'You win!'
    elif user_input == 'scissors' and computer_input == 'paper':
        return 'You win!'
    else:
        return 'You lose!'

while True:
    computer_input = random.choice(options)
    user_input = input('Enter rock, paper, or scissors: ').lower()
    if user_input not in options:
        print('invalid input, please try again.')
        continue
    print(game(user_input, computer_input))
    
    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again != 'y':
        break