import random
from GTH_ART import logo
print(logo)
print('Welcome to the Number Gaussing Game')
print("I'm Thinking between 1 to 100")
diff = input('Choose a difficulty : "EASY" OR "HARD"\n').lower()

number = random.randint(1,101)

def gauss_number(diff):
    if diff == 'hard':
        return 5
    if diff == 'easy':
        return 10

def game():
    gauss_num = gauss_number(diff)
    a = 0
    while a != number and gauss_num>0:
        print(f"YOU LEFT {gauss_num} GAUSS")
        a = int(input('Guass the number : '))
        if a == number:
            print("YOU WIN")
        elif a > number:
            print("Too High")
            gauss_num -= 1
        else:
            gauss_num -= 1
            print("Too Low")  
    if gauss_num == 0 and a != number:
        print("YOU LOSE")     
        print(f'Number is {number}') 
game()
