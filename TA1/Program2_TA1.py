digitinput = input("Enter a string that contains digits: ")

sum = 0

for i in digitinput:
    if i.isdigit():
        sum += int(i)
    
print("The sum of the digits is: ", sum)

