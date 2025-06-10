import random
def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    options = ["Rock", "Paper", "Scissors"]
    print(f"\nYou chose: {options[user - 1]}")
    print(f"Computer chose: {options[computer - 1]}")

    if user == computer:
        print("🤝 It's a tie!")
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

def play_game():
    print("=== Rock Paper Scissors Game ===")
    play_again = "y"
    
    while play_again.lower() == "y":
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)
        
        play_again = input("\nDo you want to play again? (y/n): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()