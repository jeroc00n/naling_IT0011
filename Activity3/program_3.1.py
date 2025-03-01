firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = firstname + " " + lastname
sliced = firstname[:3]

message = "Hello, {}! Welcome. You are {} years old.".format(sliced, age)

print("\nFull Name: ", fullname)
print("Sliced Name: ", sliced)
print("Greeting Message: ", message)