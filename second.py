portfolio = {}

while True:
    print("\n====== STOCK PORTFOLIO TRACKER ======")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Stock Name: ").upper()
        quantity = int(input("Quantity: "))
        buy_price = float(input("Buy Price: "))
        current_price = float(input("Current Price: "))

        portfolio[stock] = {
            "quantity": quantity,
            "buy": buy_price,
            "current": current_price
        }

        print("✅ Stock Added Successfully!")

    elif choice == "2":

        if not portfolio:
            print("Portfolio is Empty!")
            continue

        total_investment = 0
        total_value = 0

        print("\nYour Portfolio")
        print("-" * 60)

        for stock, data in portfolio.items():

            investment = data["quantity"] * data["buy"]
            value = data["quantity"] * data["current"]
            profit = value - investment

            total_investment += investment
            total_value += value

            print(f"{stock}")
            print(f"Quantity : {data['quantity']}")
            print(f"Investment : ₹{investment:.2f}")
            print(f"Current Value : ₹{value:.2f}")
            print(f"Profit/Loss : ₹{profit:.2f}")
            print("-" * 60)

        print(f"Total Investment : ₹{total_investment:.2f}")
        print(f"Current Value : ₹{total_value:.2f}")
        print(f"Overall Profit/Loss : ₹{total_value-total_investment:.2f}")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")