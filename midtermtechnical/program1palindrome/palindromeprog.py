with open('program1palindrome/numbers.txt', 'r') as file:
    lines = file.readlines()

line_number = 1

for line in lines:
    numbers = line.strip().split(',')
    total_sum = sum(int(num) for num in numbers)

    if str(total_sum) == str(total_sum)[::-1]:
        palindrome_status = "Palindrome"
    else:
        palindrome_status = "Not a palindrome"

    print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - {palindrome_status}")

    line_number += 1
