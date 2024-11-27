#currency convertor
exchange_rates = {
    "USD": {"EUR": 0.92, "GBP": 0.81, "INR": 82.3, "JPY": 148.5},
    "EUR": {"USD": 1.09, "GBP": 0.88, "INR": 89.6, "JPY": 160.9},
    "GBP": {"USD": 1.23, "EUR": 1.14, "INR": 101.5, "JPY": 180.3},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0098, "JPY": 1.78},
    "JPY": {"USD": 0.0067, "EUR": 0.0062, "GBP": 0.0055, "INR": 0.56},
}

 # List of available currencies

currencies = list(exchange_rates.keys()) 

# Start the program loop

while True:
    print("\nCurrency Converter")
    print("Available currencies:")
    
# First for loop: Display available currencies

    for currency in currencies:
        print(currency, end=" ")
    print("\n")

    print("1. Convert Currency")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()

              # Check if currencies are correct or not

        if from_currency not in currencies or to_currency not in currencies:
            print("Invalid currency. Please try again.")
            continue

        amount = float(input(f"Enter the amount in {from_currency}: "))
       
                   # Apply  conversion

        if from_currency == to_currency:
            print(f"The converted amount is the same: {amount:.2f} {to_currency}")
        else:
            rate = exchange_rates[from_currency].get(to_currency)
            if rate:
                converted_amount = amount * rate
                print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            else:
                print(f"Exchange rate from {from_currency} to {to_currency} is not available.")

                   # show conversion rate table for the source currency

        print(f"\nConversion rates for {from_currency}:")
        for target_currency ,  rate in exchange_rates[from_currency].items():
            print(f"1 {from_currency} = {rate} {target_currency}")

    elif choice == "2":
        print("Exiting the Currency Converter. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
