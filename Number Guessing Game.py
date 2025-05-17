import random
computer_choice = random.randint(0, 101)

user_choice = int(input(' Enter a number between 0-100 :'))

if not 0 <= user_choice <= 100:
    print("Your number does not fulfill the requirments ")

    
