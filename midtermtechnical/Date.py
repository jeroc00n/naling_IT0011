date_input = input("Enter the date (mm/dd/yyyy): ")

parts = date_input.split('/')

if len(parts) == 3:
    month, day, year = parts

    if month.isdigit() and day.isdigit() and year.isdigit():
        month = int(month)
        day = int(day)
        year = int(year)

        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        if 1 <= month <= 12:
            if 1 <= day <= 31:
                month_name = month_names[month - 1]
                human_readable_date = f"{month_name} {day}, {year}"
                print(f"Date Output: {human_readable_date}")
            else:
                print("Invalid day. Please enter a day between 1 and 31.")
        else:
            print("Invalid month. Please enter a month between 1 and 12.")
    else:
        print("Invalid input. Please ensure month, day, and year are numeric.")
else:
    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")