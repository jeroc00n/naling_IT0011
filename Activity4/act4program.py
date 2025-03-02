studentrec = []

while True:
    print("\n=== Student Record Management ===")
    print("1. Open File")
    print("2. Save File")
    print("3. Save as File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    choice = input("Enter your choice: ")
    
    if choice =='1':
        filename = input("Enter the file name to open: ")
        
        file = open(filename, 'r')
        studentrec = []
        
        for line in file:
            line = line.strip()
            parts = line.split(',')
            
            if len(parts) >= 5:
                student_id = parts[0]
                name = (parts[1], parts[2])
                class_standing = float(parts[3])
                major_exam_grade = float(parts[4])
    
        print("File opened successfully.")
        file.close()
    
    elif choice == '2':
        filename = input("Enter the file name to save: ")
        file = open(filename, 'w')
        for record in studentrec:
            file.write(f"{record[0]}, {record[1][0]}, {record[1][1]}, {record[2]}, {record[2]}, {record[3]}\n")
        print("File saved successfully.")
        file.close()
        
    elif choice == '3':
        filename = input("Enter the filename to save as: ")
        file = open(filename, 'w')
        for record in studentrec:
            file.write(f"{record[0]}, {record[1][0]}, {record[1][1]}, {record[2]}, {record[2]}, {record[3]}\n")
        print("File saved as successfully.")
        file.close()
        
    elif choice == '4':
        orderchoice = input("Order by (1) Last Name or (2) Grade? ")
        if orderchoice == '1':
            sortedrec = sorted(studentrec, key=lambda x: x[1][1])
        elif orderchoice == '2':
            sortedrec = sorted(studentrec, key=lambda x: (0.6 * x[2]) + 0.4 * x[3], reverse = True)
        else:
            sortedrec = studentrec
        
        print("\n=== All Students Records ===")
        for record in sortedrec:
            print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam Grade: {record[3]}")
        
    elif choice == '5':
        student_id = input("Enter Student ID: ")
        found = False
        for record in studentrec:
            if record[0] == student_id:
                print(f"ID: {record[0]}, Name: {record[1][0]} {record[1][1]}, Class Standing: {record[2]}, Major Exam Grade: {record[3]}")
                found = True
                break
            if not found:
                print("Student record not found.")
    
    elif choice == '6':
        student_id = input("Enter Student ID (6 digits): ")
        if len(student_id) != 6 or not student_id.isdigit():
            print("Invalid Student ID. It must be a 6-digit number.")
            continue
        
        firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam_grade = float(input("Enter Major Exam Grade: "))
        
        studentrec.append((student_id, (firstname, lastname), class_standing, major_exam_grade))
        print("Record added successfully.")
        
    elif choice == '7':
        student_id = input("Enter Student ID to edit: ")
        found = False

        for index, record in enumerate(studentrec):

            if record[0] == student_id:

                print("Editing record:")

                firstname = input(f"Enter First Name (current: {record[1][0]}): ") or record[1][0]

                lastname = input(f"Enter Last Name (current: {record[1][1]}): ") or record[1][1]

                class_standing = input(f"Enter Class Standing Grade (current: {record[2]}): ")

                major_exam_grade = input(f"Enter Major Exam Grade (current: {record[3]}): ")
                

                class_standing = float(class_standing) if class_standing else record[2]

                major_exam_grade = float(major_exam_grade) if major_exam_grade else record[3]


                studentrec[index] = (student_id, (firstname, lastname), class_standing, major_exam_grade)

                print("Record updated successfully.")

                found = True
                break

        if not found:
            print("Student record not found.")


    elif choice == '8': 
        student_id = input("Enter Student ID to delete: ")
        found = False

        for index, record in enumerate(studentrec):

            if record[0] == student_id:
                del studentrec[index]
                print("Record deleted successfully.")
                found = True
                break

        if not found:
            print("Student record not found.")

    elif choice == '9':  
        print("Exiting the program.")
        break
    
    else:

        print("Invalid choice. Please try again.")
                
                
            
    