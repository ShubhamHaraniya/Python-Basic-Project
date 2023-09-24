from operator import index
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

noto_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(noto_dict)
name = input("Enter Name : ").upper()
main = [noto_dict[letter] for letter in name ]
print(main)