import random
from Hangman_wordlist import word_list
from Hangman_art import logo,stages
from colorama import Fore,Back

print(Fore.RED+logo)
choice_word = random.choice(word_list)
chance = 6
word_list = []
for wl in range(1,len(choice_word)+1):
    word_list.append("_")
print(Fore.GREEN+"")    
print(word_list)
print("")


while chance > 0 and "_" in word_list:
    count = 0
    attend = 0
    gauss = input(Fore.LIGHTMAGENTA_EX+"Gauss the letter :\n").lower()
    for letter in choice_word:
        attend += 1  
        if letter == gauss:
            count += 1
            word_list[attend-1] = gauss
            print(Fore.GREEN + "")
    if count != 0:       
        print(Fore.LIGHTCYAN_EX+"You Guass Correctly. " + gauss + " in word.")
        print(Fore.GREEN)
        print(word_list)
        print('\nYour current Stage')
        print(stages[6-chance])
        print('\n')
        if "_" not in word_list:
            print("Congrts, YOU WIN\n"+Fore.WHITE)
            print(f'WORD IS {choice_word}')
            pass
            
    if count == 0:
        print("\n"+Fore.YELLOW+"it's wrong"+Fore.WHITE)
        chance -= 1
        if chance > 0 :
            print(Fore.RED)
            print('\nYour current Stage')
            print(stages[6-chance])
        else:
            print(stages[6-chance])
            print(f'{Fore.GREEN}WORD IS : {choice_word}\n {Fore.WHITE}')
            print(Fore.RED+"\nGAME OVER\n"+Fore.WHITE)
    
    
    
        

