lastname = input("Enter your last name: ")
firstname = input("Enter your first name: ")
age = input("Enter your age: ")
contactnum = input("Enter your contact number: ")
course = input("Enter your course: ")

studentinfo = (
    f"Last Name: {lastname} \n"
    f"First Name: {firstname} \n"
    f"Age: {age} \n"
    f"Contact Number: {contactnum} \n"
    f"Course: {course} \n"
)

with open("Activity3/students.txt", "a") as file:
    file.write(studentinfo)
    
print("\nStudent information has been saved successfully!")