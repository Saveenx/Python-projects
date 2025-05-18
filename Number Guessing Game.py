import random
computer_choice = random.randint(0, 101)

while True :
 try:
    user_choice = int(input('Enter a number between 0-100: '))
    if user_choice < computer_choice :
     print("Youre too low !")
    elif user_choice > computer_choice:
     print("Your too high !")
    else:
     print("congrats...You win !")
     break
 except ValueError:
   print("Invalid input! Please enter a valid number.")

    
