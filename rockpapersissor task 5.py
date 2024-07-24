import random

def taking_inputof_user():
    input_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while input_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        input_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return input_choice

def response_of_computer():
    return random.choice(['rock', 'paper', 'scissors'])
 
def Winner(user_input, computer_input):
    
    if user_input == computer_input :
        return "It's a Tie!"
        
    elif (user_input == 'rock' and computer_input == 'scissors'):
        return 'Congratulations! You Win'
    elif (user_input == 'scissors' and computer_input == 'paper'):
        return 'Congratulations! You Win'
    elif (user_input == 'paper' and computer_input == 'rock'):
        return 'Congratulations! You Win'
        
    else:
        return 'Oops sorry u lost!! '

def Game():
    user_input = taking_inputof_user()
    computer_input = response_of_computer()
    
    print('Your choice is : ', user_input)
    print('Computer choice is : ', computer_input)
    
    result = Winner(user_input,computer_input)
    print(result)
 
    play_input = input('WANT TO PLAY AGAIN? (Yes or No):').lower()
    if play_input == 'yes':
        Game()
    else:
        pass
    
Game()