import random

choices = ["rock", "paper", "scissor"]  # choises and suitable emojies
emojes = {'rock': '🧱', 'scissor': '✂', 'paper': '🧻'}

# user and computer inputs
while True:
# Main game loop
        # Get valid user input
    while True:
            user_input = input("rock, paper, or scissor: ").lower()
            if user_input in choices:
                break
            print("Invalid input, please try again.")
                

            computer_input = random.choice(choices)

    print(f"Computer chose {computer_input} {emojes[computer_input]}")
    print(f"Computer chose {user_input} {emojes[user_input]}")

    if user_input == computer_input:
        print("It's a tie!")
    elif user_input == "rock" and computer_input == "scissor":
        print("You win!")  # determining winner
    elif user_input == "scissor" and computer_input == "rock":
        print("You lose!")
    elif user_input == "paper" and computer_input == "scissor":
        print("You lose!")
    elif user_input == "scissor" and computer_input == "paper":
        print("You win!")
    elif user_input == "rock" and computer_input == "paper":
        print("You lost!")
    else:
        print("You win!")

    if input("Play again? (y/n): ").lower() != 'y':
     break