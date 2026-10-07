prices = [100, 200, 300]
discount = 10
Total_prices = []
for price in prices:
    final_price = price - (price * discount/100)
    Total_prices.append(final_price)
print(Total_prices)