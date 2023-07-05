#Here is where the menu list is created.
menu = ['Coffee', 'Tea', 'Sandwich', 'Salad']

#Here is where the vocabulary with stock values is created.
stock = {
    'Coffee': 100,
    'Tea': 50,
    'Sandwich': 80,
    'Salad': 70
}

#Here is where the price vocabulary is created.
price = {
    'Coffee': 2.5,
    'Tea': 1.8,
    'Sandwich': 5.0,
    'Salad': 4.5
}

#Here is the calculation of the total cost of inventory.
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

#Here we output the result.
print("The total value of the stock in the café:", total_stock)