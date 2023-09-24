from colorama import Fore
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(Fore.RED+'---------------------------------------------------------------------------------------')
print(Fore.MAGENTA+"Welcome to the Password Generator!")
print(Fore.RED+'---------------------------------------------------------------------------------------')
no_letters= int(input(Fore.CYAN+"How many letters would you like in your password? : ")) 
no_symbols = int(input(f"How many symbols would you like? : "))
no_numbers = int(input(f"How many numbers would you like? : "))
print(Fore.RED+'---------------------------------------------------------------------------------------')

Password_list = []

for letter in range(1,no_letters+1):
    Password_list.append(random.choice(letters))
for symbol in range(1,no_symbols+1):
    Password_list.append(random.choice(symbols))
for number in range(1,no_numbers+1):
    Password_list.append(random.choice(numbers))

random.shuffle(Password_list)
Password =""
for p in Password_list:
    Password += p    
print(Fore.GREEN+Password)    
print(Fore.RED+'---------------------------------------------------------------------------------------')