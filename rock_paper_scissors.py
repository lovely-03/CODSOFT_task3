import random

def user_choice():
    #This function takes input from the user
    user_input = input("Chose rock, paper, or scissors: ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        user_input = input("Enter choice (rock, paper, scissors): ").lower()
    return user_input

def computer_choice():
    #This function generates a random choice for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(choice1, choice2):
    #This function determines the winner
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or (choice1 == 'paper' and choice2 == 'rock') or (choice1 == 'scissors' and choice2 == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    while True:
        choice1 = user_choice()
        choice2 = computer_choice()
        
        print(f"\nYou chose: {choice1}")
        print(f"Computer chose: {choice2}\n")
        
        #Displaying result
        result = determine_winner(choice1, choice2)
        print(result)
        
        #Ask the user if they want to play another round
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


play_game()

