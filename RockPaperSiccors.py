import random

def get_player_choice():
    # Ask player for their choice
    choice = input("Enter your choice (rock,paper,siccors): ").lower()
    return choice

# Get computer's choice

def get_computer_choice():
    choices = ("rock"), ("paper"), ("siccors")
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "siccors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "siccors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(f"You chose {player_choice}, computer chose {computer_choice}. {result}")

if __name__ == "__main__":
    play_game()

