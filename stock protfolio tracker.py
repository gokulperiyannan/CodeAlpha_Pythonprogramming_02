stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

# Function to calculate total investment
def stock_portfolio_tracker():
    total_investment = 0
    portfolio = {}

    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break

        if stock_name in stock_prices:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            investment = stock_prices[stock_name] * quantity
            portfolio[stock_name] = investment
            total_investment += investment
        else:
            print("Stock not found. Please enter a valid stock symbol.")

    print("\nYour Investment Portfolio:")
    for stock, amount in portfolio.items():
        print(f"{stock}: ${amount}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional: save results to a file
    save_option = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save_option == "yes":
        with open("portfolio.txt", "w") as file:
            for stock, amount in portfolio.items():
                file.write(f"{stock}: ${amount}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Portfolio saved successfully to 'portfolio.txt'.")

# Run the program
stock_portfolio_tracker()