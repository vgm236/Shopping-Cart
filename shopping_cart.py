# shopping_cart.py

import datetime

# LIST OF PRODUCTS
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# INPUT IDENTIFIER

## CREATE NEW LIST - FILTERING
def list_products(list_id, list_products):
    matching_products = [p for p in list_products if str(p["id"]) == str(list_id)]
    matching_product = matching_products[0]
    return matching_product

## WORKING INTO USER CHOICE 
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id == "DONE":
        break
    while selected_id not in str(list_products):
        print("ID Not found. Please try again.")
        break
    else:
        selected_ids.append(selected_id)


# INTRODUCTION
print("---------------------------")
print("WELCOME TO BRAZIL MARKET")
print("WWW.BRAZILMARKET.COM.BR")
print("---------------------------")

# PRINT DATE AND TIME
now = datetime.datetime.now()
print("CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
print("---------------------------")

# SELECTED PRODUCT LIST AND PRICES
print("SELECTED PRODUCTS:")

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

subtotal_price = 0

for selected_id in selected_ids:
    matching_product = list_products(selected_id, products)
    subtotal_price = subtotal_price + matching_product["price"]
    print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

# PRICE WITH TAX

TAX_RATE = 0.06

tax = subtotal_price * TAX_RATE

total_price = subtotal_price + tax

print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total_price))

# END OF THE PROGRAM
print("---------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------")

#>(shopping-env)  --->> python shopping_cart.py
#>Please input a product identifier: 1
#>Please input a product identifier: 8
#>Please input a product identifier: 6
#>Please input a product identifier: 8
#>Please input a product identifier: 8
#>Please input a product identifier: 16
#>Please input a product identifier: 12
#>Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2019-06-06 11:31 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------