file_path = "/mnt/data/currency.csv"

exchange_rates = {}
with open(file_path, "r") as file:
    next(file)  
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            code, name, rate = parts[0], parts[1], float(parts[2])
            exchange_rates[code] = (name, rate)


dollars = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

if currency in exchange_rates:
    name, rate = exchange_rates[currency]
    converted_amount = dollars * rate
    print(f"\nDollar: {dollars} USD")
    print(f"{name}: {converted_amount}")
else:
    print("Invalid currency code. Please check and try again.")