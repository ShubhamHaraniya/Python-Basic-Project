import random
from colorama import Fore,Back
user_win = 0
com_win = 0
tie = 0

options = ["rock", "paper","scissor"]

print("\n"+Fore.YELLOW +"Welcome to the game")
while True:
    user_input = input(Fore.GREEN +"What do you want to choose :" + Fore.CYAN + "rock or paper or scissor or quit the game?\n").lower()
    if user_input == "quit":
        print("you are quit the game")
        break
    if user_input not in options:
        print("please enter valid oparator")
        continue
    
    ran_num = random.randint(0,2)
    
    com_input = options[ran_num]
    print(Fore.LIGHTMAGENTA_EX+ "You choose " + user_input)
    print( "Computer choose " + com_input)
        
    if user_input == com_input: 
         print("game is tie")
         tie += 1
    elif user_input == options[0] and com_input == options[1]:
        print("YOU LOSE")
        com_win += 1
    elif user_input == options[0] and com_input == options[2]:
        print("YOU WIN")
        user_win += 1
    elif user_input == options[2] and com_input == options[0]:
        print("YOU LOSE")
        com_win += 1
    elif user_input == options[1] and com_input == options[0]:
        print("YOU WIN")
        user_win += 1
    elif user_input == options[1] and com_input == options[2]:
        print("YOU LOSE")
        com_win += 1
    else:
        print("YOU WIN")
        user_win += 1
            
    print("\nUser Win : " + str(user_win))
    print("Computer Win : " + str(com_win))
    print("Tie : "+ str(tie) + "\n")