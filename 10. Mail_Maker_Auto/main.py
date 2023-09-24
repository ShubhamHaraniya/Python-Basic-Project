with open("C:\\Users\\sphar\\Desktop\\Python 101\\Project\\Mail_Maker_Auto\\s.txt") as names :
    for name in names.readlines():
        with open(f"C:\\Users\\sphar\\Desktop\\Python 101\\Project\\Mail_Maker_Auto\\Letters\\{name.strip()}_Letter.txt" , mode='w') as Letter:
            Letter.write(f'''Dear {name.strip()}\nYou are invite to my birthday party on this sunday\nI hope you will come\nThank You So Much''')
            