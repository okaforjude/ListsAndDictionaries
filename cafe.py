
# This program calculates the total stock of items in a cafe

menu = ["salad", "donut", "croissant", "eggs"]

stock = {"salad" : 15, "donut" : 20, "croissant" : 10, "eggs" : 30}

price = {"salad" : 10, "donut" : 5, "croissant" : 5, "eggs" : 15}

total_stock = 0


for item in menu:

    item_value = (stock[item] * price[item])

    total_stock += item_value

print(total_stock)
