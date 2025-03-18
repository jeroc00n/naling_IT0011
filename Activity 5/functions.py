def divide(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a/b

def expo(a, b):
    return a**b

def rem(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a % b

def summ(a, b):
    if b <= a:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def menu():
    print("\nMenu:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")
    
def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program. Thank you for using the program!")
            break
        
        if choice not in ['D', 'E', 'R', 'F']:
            print("Invalid choice. Please only choose between: D, E, R, F, and Q.")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 'D':
            result = divide(num1, num2)
        elif choice == 'E':
            result = expo(num1, num2)
        elif choice == 'R':
            result = rem(num1, num2)
        elif choice == 'F':
            result = summ(num1, num2)
        
        if result is not None:
            print("Result: ", result)

main()