#Items in our cafe
menu = ["banana", "orange", "apple", "pear"] 

#our stock
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#prices for each item in our stock
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item] * stock[item]
    return total


print(compute_bill(menu))