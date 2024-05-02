name=input("What is your name?")
takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00
total=0


print("Welcome to the takeaway delivery service.")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print("Thank you",name, "your order is as follows")

def take(item):
    for item in order:
        print(takeaway_menu[item-1])
        total=total+takeaway_prices[item-1]
    total=total+delivery_fee
    return total
print(total)    
    

