print("""This is a program that will count the 
vowels, consonants, spaces, and other characters
in your inputted string.""")
print("\n")

vowelcount = 0
conscount = 0
spacecount = 0
othercharcount = 0

vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
strinput = input('Enter an input: ')
print("\n")

for i in strinput:
    if i in vowels:
        vowelcount += 1
    elif i in consonants:
        conscount += 1
    elif i == ' ':
        spacecount += 1
    else:
        othercharcount += 1

print("The # of vowels in the string: ", vowelcount)
print("The # of consonants in the string: ", conscount)
print("The # of whitespaces on the string: ", spacecount)
print("The # of special/other characters in the string: ", othercharcount)

