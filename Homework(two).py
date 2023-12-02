print("Welcome to the new online ordering system.\n")
Name=input("What is name of the user")
#This program is a simple ordering system
acount=input("Add customer balance")
acount=float(acount)
items_count=input("How many items are you buying")
items_count=float(items_count)
if items_count<=0:
    print("This is an invaild option please choose a number over 0")
else:
    Total=0+items_count
    counter=0
    total_cost=0
    counter2=0
    while counter!=items_count:
        price_of_item = float(input("Enter the price of item {}".format(items_count)+ ": € "))
        total_cost+=price_of_item
        items_count=items_count-1
   
    Left=acount-total_cost

    if acount<total_cost:
        Need=total_cost-acount
        Need=str(Need)
        print("The customer doesnt have enough credit in their acount,they still owe:"+Need)
    else:
        Left=str(Left)
        acount=str(acount)
        print("You entered",Total,"items and the total is €",total_cost)
        print("What is the customer acount balance €"+acount)
        print("Your remaining balance:"+Left)
    print("The staff that processed your order was:"+Name)

    


