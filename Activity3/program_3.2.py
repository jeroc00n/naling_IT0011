firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

fullname = firstname + " " + lastname

fullnameup = fullname.upper()
fullnamelow = fullname.lower()

fullnamelen = len(fullname)

print("\nFull Name: ", fullname)
print("Full Name (Uppercase): ", fullnameup)
print("Full Name (Lowercase): ", fullnamelow)
print("Length of Full Name: ", fullnamelen)