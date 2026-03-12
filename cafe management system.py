menu={1:{"item":"coffee","price":80},
   2: {"item":"Tea","price":40},
   3: {"item":"sandwish","price":120},
   4: {"item":"burer","price":140},
   5: {"item":"Pizza","price":250},}
total_bill=0
order_list=[]
print("Welcome to RAHUL CAFE")

while True:
    print("\n Menu")
    for key in menu:
        print(f"{key}.{menu[key]['item']}-₹{menu[key]['price']}")
    
    try:
        choice=int(input("enter item number to order:"))
        if choice in menu:
            quantity=int(input("enter quantity:"))
            item_total= menu[choice]['price']*quantity
            total_bill+=item_total
            
            order_list.append((menu[choice]['item'],quantity,item_total))
            print(f"{menu[choice]['item']}added to cart.")
        else:
            print("invalid choice, please select from menu.")
    except ValueError:
        print("please enter valid numbers.")
        
    more=input("do you want to order more(yes/no):").lower()
    if more!="yes":
        break

print("-----final bill-----")
for item,qty,price in order_list:
    print(f"{item}*{qty}=₹{price}")
print(f"total amount to pay: ₹{total_bill}")
print("Thank You visit Again🙏")
    