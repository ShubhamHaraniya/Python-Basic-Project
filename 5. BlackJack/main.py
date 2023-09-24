import random
from art import logo
print(logo)
Want = input("Do you want to play backjake : 'Yes' or 'No' \n").lower()
user_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
comp_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
you_win = 0
comp_win = 0
draw = 0
again = True
while again:
    if Want == 'yes':
        user_Card1 = user_cards[random.randint(0,11)]
        user_Card2 = user_cards[random.randint(0,11)] 
        user_Card3 = user_cards[random.randint(0,11)] 
        User_Card = [user_Card1,user_Card2,user_Card3]    
        Comp_Card1 = comp_cards[random.randint(0,11)]
        Comp_Card2 = comp_cards[random.randint(0,11)] 
        Comp_Card3 = comp_cards[random.randint(0,11)] 
        Comp_Card = [Comp_Card1,Comp_Card2,Comp_Card3]
    
        print(f'Your Card : {(User_Card[0],User_Card[1])}')
        print(f'Comp Card : {(Comp_Card[0])}')
        C_3= input("Do you want one more card : 'Yes' or 'No'\n").lower()
        if C_3 == 'yes':
            sum_user = User_Card[0]+User_Card[1]+User_Card[2]
            sum_comp = Comp_Card[0]+Comp_Card[1]+Comp_Card[2]
            if sum_user > 22:
                if 11 in User_Card:
                    a = 0
                    for l in User_Card:
                        while sum_user>22:
                            if l == 11:
                                User_Card[a] = 1
                                sum_user = User_Card[0]+User_Card[1]+User_Card[2]
                            a += 1     
            if Comp_Card[0]+Comp_Card[1] > 16: 
               print(f'Your Card : {(User_Card[0],User_Card[1],User_Card[2])}')
               print(f'Comp Card : {(Comp_Card[0],Comp_Card[1])}')
               if sum_user > 22:
                print("YOU LOSE!")
                comp_win += 1
               elif sum_user > Comp_Card[0]+Comp_Card[1]:
                print("YOU WON!")
                you_win += 1
               elif sum_user == Comp_Card[0]+Comp_Card[1]:
                print("MATCH DRAW!")
                draw += 1
               else:
                print("YOU LOSE!")
                comp_win += 1
            else:
                if sum_comp > 22:
                    if 11 in Comp_Card:
                        a = 0
                        for l in Comp_Card:
                            while sum_comp>22:
                                if l == 11:
                                    Comp_Card[a] = 1
                                    sum_comp = Comp_Card[0]+Comp_Card[1]+Comp_Card[2]
                                a += 1  
                print(f'Your Card : {(User_Card[0],User_Card[1],User_Card[2])}')
                print(f'Comp Card : {(Comp_Card[0],Comp_Card[1],Comp_Card[2])}')                
                if sum_user > 22 and  sum_comp > 22:
                    print('MATCH DRAW') 
                    draw += 1
                elif sum_user > 22 and sum_comp < 22:
                    print('YOU LOSE!')
                    comp_win += 1
                elif sum_user < 22 and sum_comp > 22:       
                    print('YOU WIN!')
                    you_win += 1
                elif sum_user > sum_comp:
                    print('YOU WIN!') 
                    you_win += 1
                elif sum_user < sum_comp:   
                    print('YOU LOSE!')
                    comp_win += 1
                else :
                    print('MATCH DRAW') 
                    draw += 1     
        if C_3 == 'no':
            print(f'Your Card : {(User_Card[0],User_Card[1])}')
            print(f'Comp Card : {(Comp_Card[0],Comp_Card[1])}')
            if User_Card[0]+User_Card[1] > Comp_Card[0]+Comp_Card[1]:
                print("YOU WIN!")
                you_win += 1
            elif User_Card[0]+User_Card[1] < Comp_Card[0]+Comp_Card[1]:
                print("YOU LOSE!")   
                comp_win += 1
            else :
                print("MATCH DRAW!")    
                draw += 1 
    want_agian = input("Do you want to play again: 'Yes' , 'No'\n")
    if want_agian == 'yes':
        again = True
    if want_agian == 'no':
        again = False

print("\nALLOVER SCORE")
print(f'You win {you_win} Times')
print(f'Computer win {comp_win} Times')
print(f'Match Draw {draw} Times')