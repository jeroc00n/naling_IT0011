firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = firstname + " " + lastname
sliced = firstname[:3]

message = f"Hello, {sliced}! Welcome. You are {age} years old."

print("\nFull Name: ", fullname)
print("Sliced Name: ", sliced)
print("Greeting Message: ", message)