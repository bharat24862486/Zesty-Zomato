dish=[{"ID":1,"Name":"samosa","Quantity":10,"Price":20},{"ID":2,"Name":"momo","Quantity":5,"Price":10},
      {"ID":3,"Name":"pizza","Quantity":8,"Price":100}]


orders=[]

def Add_dish():
    name=(input("Enter Dish Name: "))
    Id=int(input("Enter Dish ID: "))
    price=int(input("Enter Dish Price: "))
    quantity=int(input("Enter Dish Quantity: "))

    ob={
        "ID":Id,
        "Name":name,
        "Price":price,
        "Quantity":quantity

    }


    for i in range(len(dish)):
        if dish[i]["ID"]==Id:
            print("\n")
            print("Dish already exist with this Id")
            return 


    dish.append(ob)
    print("\n")
    print("Dish Added Successfully !!")


def Show_Menu():
    print(dish)

def Remove_dish():
    print("\n")
    Id=int(input("Enter Dish ID: "))

    for i in range(len(dish)):
        if dish[i]["ID"]==Id:
            dish.pop(i)
            print("Dish Removed Successfully !!")
            return 
        
    print("Item not found!!")


def Update_Availablity():
    Id=int(input("Enter Dish ID: "))
    quantity=int(input("To add more quantity: "))

    for i in dish:
        if i["ID"]==Id:
            a = i["Quantity"]
            a+=quantity
            i["Quantity"] = a
            print()
            print("Dish Quantity has updated Successfully !!")
            return 
        
    print("Item not found!!")

    # print("remove")

def New_Order():
    Id=int(input("Enter Dish ID: "))
    yourname = input("Enter your Name: ")
    quantity=int(input("How much in quantity: "))
    obj={}
    for i in dish:
        if i["ID"]==Id:
            a = i["Quantity"]
            a-=quantity
            i["Quantity"] = a
            print()
            
            
            obj["ItemName"] = i["Name"]
            obj["Price"] = i["Price"]
            obj["Quantity"] = quantity
            obj["ID"]=i["ID"]
            obj["Name"] = yourname
            obj["Status"] = "Pending"
            p = i["Price"]
            q = quantity
            t = p*q
            obj["Total"] = t
            name = i["Name"]
            # print(obj)
            print()
            print(f"{yourname} has just ordered {name}, at quantity {quantity} and your total is {t}")
            print()
            print(f"\n Your order in pending state,please press 6 to confirm your order!! \n")
            orders.append(obj)
            if i["Quantity"] == 0:
                dish.remove(i)
            return 
        
    print("Item Out of Stock")

def Update_order_status():
    name=(input("Enter Order Name: "))

    for i in orders:
        if i["Name"]==name:
            
            i["Status"] = "Confirmed"
            print()
            print(f"\n your order is confirmed \n")
            return 

    print("order name not found")

def Review_Order():
    print(orders)

while True:
    print("Welcome to Zesty Zomato")
    print("Choose 1 option out of this")
    print("1. Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Availablity") 
    print("5. New Order") 
    print("6. Update order Status")
    print("7, Review all orders")
    print("8. Exit")

    choice = int(input("choose you input: "))

    if choice==1:
        Show_Menu()

    elif choice==2:
        print("\n")
        Add_dish()

    elif choice==3:
        Remove_dish()

    elif choice==4:
        Update_Availablity()

    elif choice==5:
        New_Order()  

    elif choice==6:
        Update_order_status()

    elif choice==7:
        Review_Order()

    elif choice==8:
        print("You have successfully quit!! ")
        break;
    else:
        print("Invalid Input")
        continue