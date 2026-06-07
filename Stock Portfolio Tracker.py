stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}
portfolio = {}
total_investment = 0
print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))
n = int(input("Enter the number of stocks you want to add: "))
for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available!")
print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")
print("\nTotal Investment Value = $", total_investment)
with open("portfolio_report.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("======================\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock}: {quantity} shares × ${price} = ${investment}\n")
    file.write(f"\nTotal Investment Value = ${total_investment}")
print("\nReport saved successfully as 'portfolio_report.txt'")