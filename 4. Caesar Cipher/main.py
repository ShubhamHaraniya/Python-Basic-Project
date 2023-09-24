from CC_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
while direction != "encode" and direction != "decode":
    print("\nPLEASE, Enter the valid action")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()   
if direction == "encode" or direction == "decode": 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    

def caesar():
    if direction == "encode":
        new_word = ''
        for letter in text:
            old_position = alphabet.index(letter)
            new_position = old_position + shift
            if new_position>25:
                new_position = new_position - 26
                new_word += alphabet[new_position]
            else:
                new_word += alphabet[new_position]    
        print(f'Your word is {new_word}')
    elif direction == "decode":
        new_word = ''
        for letter in text:
            old_position = alphabet.index(letter)
            new_position = old_position - shift
            new_word += alphabet[new_position]    
        print(f'Your word is {new_word}')
    else:
        print("PLEASE, Enter the valid direction")   

caesar()
again = input('Do you want to do again : "Yes" or "No"?\n').lower()

while again=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != "encode" and direction != "decode":
        print("\nPLEASE, Enter the valid action")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()   
    if direction == "encode" or direction == "decode": 
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    caesar()
    again = input('Do you want to do again : "Yes" or "No?\n')