menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

##Task 1 - 1."Menu Analysis"

# Get unique categories
categories = set()
for item in menu:
    categories.add(menu[item]["category"])
#Loop through categories
for c in categories:
    print("===", c, "===")

    for item in menu:
        if menu[item]["category"] == c:
            price = menu[item]["price"]
            available = menu[item] ["available"]

            if available:
                status = "Available"
            else:
                status = "Unavailable"
            print(item,"Rs." + str(price),"[" + status + "]")

            print()

#Task 1-2.Compute required values

# Total items 
print("Total items:", len(menu))

#Available items 
count=0
for item in menu:
    if menu[item]["available"]:
        count += 1
print("Available items:", count)

# Most expensive item
max_price = 0
max_item =""

for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        max_item = item
print("Most expensive:", max_item, "Rs." + str(max_price))

# Items under 150
print("Items under Rs.150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, "Rs." + str(menu[item]["price"]))


##------Task 2 - Cart operations

# Empty cart
cart = []

# Function to add item
def add_item(name, qty):
    if name not in menu:
        print("Item not in menu")
        return

    if menu[name]["available"] == False:
        print("Item is unavailable")
        return

    # Check if item already in cart
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            print(name, "quantity updated")
            return

    # If not in cart, add new
    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })
    print(name, "added to cart")


# Function to remove item
def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            print(name, "removed")
            return
    print("Item not in cart")


# Function to update quantity
def update_quantity(name, qty):
    for item in cart:
        if item["item"] == name:
            item["quantity"] = qty
            print(name, "quantity updated")
            return
    print("Item not in cart")


# Function to print cart
def print_cart():
    print("Cart:", cart)


# ---- Simulation ----

add_item("Paneer Tikka", 2)
print_cart()

add_item("Gulab Jamun", 1)
print_cart()

add_item("Paneer Tikka", 1)   # should update quantity
print_cart()

add_item("Mystery Burger", 1) # not in menu
print_cart()

add_item("Chicken Wings", 1)  # unavailable
print_cart()

remove_item("Gulab Jamun")
print_cart()


# Final Summary
print("\nOrder Summary")
total = 0

for item in cart:
    cost = item["quantity"] * item["price"]
    total += cost
    print(item["item"], "x", item["quantity"], "=", cost)

print("Total =", total)


#----Task 3- Inventory Tracker with Deep copy-------
#----3.1 Deep copy --------
import copy

# Original inventory
inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2}
}

# Deep copy
inventory_copy = copy.deepcopy(inventory)

# Modify copy
inventory_copy["Paneer Tikka"]["stock"] = 2

print("Original Inventory:")
print(inventory)

print("\nCopied Inventory:")
print(inventory_copy)

#-----3.2 Deduct stock using cart------
for i in cart:
    name = i["item"]
    qty = i["quantity"]
    
    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] = inventory[name]["stock"] - qty
    else:
        print("Warning:", name, "only", inventory[name]["stock"], "left")
        inventory[name]["stock"] = 0

#-----3.3 Reorder alert-----
for item in inventory:
    stock = inventory[item]["stock"]
    level = inventory[item]["reorder_level"]
    
    if stock <= level:
        print("⚠ Reorder Alert:", item, "- Only", stock, "units left")

#------3.4 Print inventory------
print("\nFinal Inventory:")
for item in inventory:
    print(item, "->", inventory[item])

print("\nBackup Inventory:")
for item in inventory_copy:
    print(item, "->", inventory_copy[item])


#----Task 4 - Daily sales log Analysis-----
# Sample sales_log (use your given one if already provided)
sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 220},
        {"order_id": 2, "items": ["Gulab Jamun"], "total": 210}
    ],
    "2025-01-02": [
        {"order_id": 3, "items": ["Paneer Tikka"], "total": 180}
    ]
}

# 1. Total revenue per day
print("Revenue per day:")
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    print(date, "=", total)


# 2. Best-selling day
best_day = ""
max_revenue = 0

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]

    if total > max_revenue:
        max_revenue = total
        best_day = date

print("\nBest selling day:", best_day)


# 3. Most ordered item
item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

most_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        most_item = item

print("Most ordered item:", most_item)


# 4. Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun"], "total": 300},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 250}
]

print("\nAfter adding new day:")

# Reprint revenue per day
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    print(date, "=", total)


# Recalculate best day
best_day = ""
max_revenue = 0

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]

    if total > max_revenue:
        max_revenue = total
        best_day = date

print("New best selling day:", best_day)


# 5. Numbered list using enumerate
print("\nAll Orders:")

count = 1
for date in sales_log:
    for order in sales_log[date]:
        print(count, ".", date, "Order#", order["order_id"], "-", order["total"], "- Items:", order["items"])
        count += 1
