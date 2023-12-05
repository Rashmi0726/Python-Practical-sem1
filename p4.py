"""WAP that accepts a character and performs the following:
a. print whether the character is a letter or numeric digit or a special character
b. if the character is a letter, print whether the letter is uppercase or lowercase
c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output
is NINE)"""
ch=input("Enter a character:")
if ch.isalpha():
    print(ch,"is a letter")
    if ch.isupper():
        print(ch,"is a uppercase")
    elif ch.islower():
        print(ch,"is a lowercase")
elif ch.isnumeric():
    print(ch,"is a numeric digit")
    Name={'1':"ONE",'2':"TWO",'3':"THREE",'4':"FOUR",'5':"FIVE",'6':"SIX",'7':"SEVEN",'8':"EIGHT",'9':"NINE",'0':"ZERO"}
    if ch in Name.keys():
        print(Name[ch])
else:
    print(ch,"is a special character")