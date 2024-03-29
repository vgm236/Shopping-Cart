# shopping_cart.py

import datetime # helps to give date and time correctly
import operator # helps to sort correctly
import os.path # helps to save in a different folder
import gspread # helps to integrate with google sheets

from dotenv import load_dotenv # packages for email
from sendgrid import SendGridAPIClient # packages for email
from sendgrid.helpers.mail import Mail # packages for email

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
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25},
    {"id":21, "name": "Organic Bananas", "department": "fruits", "aisle": "juice nectars", "price": 0.79}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# INPUT IDENTIFIER

## CREATE NEW LIST - FILTERING
def list_products(list_id, all_products):
    matching_products = [p for p in all_products if str(p["id"]) == str(list_id)]
    matching_product = matching_products[0]
    return matching_product

## CREATE VALID IDS
valid_ids = sorted(products, key=operator.itemgetter('id'))


## WORKING INTO USER CHOICE 
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id == "DONE":
        break
    elif selected_id == "Done":
        break
    elif selected_id == "done":
        break
    while selected_id not in str(valid_ids):
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

TAX_RATE = 0.0874

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

# WRITING RECEIPT

save_path = 'C:/Users/Owner/Desktop/NYU-MBA/Programming/Files/Shopping-Cart/receipts'

file_name = os.path.join(save_path, now.strftime("%Y-%m-%d-%H-%M-%S-%f") +".txt")
with open(file_name, "w") as file: # "w" means "open the file for writing"
    file.write("---------------------------")
    file.write("\n")
    file.write("WELCOME TO BRAZIL MARKET")
    file.write("\n")
    file.write("WWW.BRAZILMARKET.COM.BR")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write("CHECKOUT AT: " + now.strftime("%Y-%m-%d %I:%M:%S %p"))
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write("SELECTED PRODUCTS:")
    file.write("\n")
    for selected_id in selected_ids:
        matching_product = list_products(selected_id, products)
        subtotal_price = subtotal_price + matching_product["price"]
        file.write(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")" +"\n")
    file.write("---------------------------")
    file.write("\n")  
    file.write("SUBTOTAL: " + to_usd(subtotal_price))
    file.write("\n")  
    file.write("TAX: " + to_usd(tax))
    file.write("\n")  
    file.write("TOTAL: " + to_usd(total_price))
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")  
    file.write("THANKS, SEE YOU AGAIN SOON!")
    file.write("\n")  
    file.write("---------------------------")
    file.write("\n")   
    # PRINTING RECEIPT (from https://stackoverflow.com/questions/12723818/print-to-standard-printer-from-python)
    os.startfile(file_name, "print")

load_dotenv()
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

#E-MAIL OPTION
with open(file_name, "r") as file: # "r" means "open the file for reading"
    contents = file.read()

subject = "Your receipt from Brazil Market"
html_content = contents

while True:
    selected_id = input("Do you want your receipt emailed to you? (y or n): ")
    if selected_id == "y":
        message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)
        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))
        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)
        except Exception as e:
            print("OOPS", e.message)
        break

    elif selected_id == "Y":
        message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS, subject=subject, html_content=html_content)
        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))
        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)
        except Exception as e:
            print("OOPS", e.message)
        break
    else:
        break


print(contents)




