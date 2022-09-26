import json
import datetime


def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "password": password,
        "age": age,
        "phone number": phn,
        "order history": {}
        
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except json.JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"


def user_order_history(user_json, user_id):
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            print("Order History")
            print("Date | Order")
            for i, j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    return False


count = 0


def user_place_order(user_json, food_json, user_id, food_name, quantity):
    global count
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    file = open(user_json, "r+")
    content = json.load(file)
    file1 = open(food_json, "r+")
    content1 = json.load(file1)
    flag = 0
    food_price = 0
    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no_of_plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no_of_plates"] -= quantity
                        if date not in content[j]["order history"]:
                            content[j]["order history"][date] = [
                                content1[i]["name"]]
                            flag = 1
                            count = count+1
                            food_price = content1[i]["price"]*quantity
                            print("Food_price:", food_price)
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
                            flag = 1
                            count = count+1
                            food_price = content1[i]["price"]*quantity
                            print("Food_price:", food_price)
            else:
                print("Pls Enter less quantity")
                break
    if flag == 0:
        print("Be ready for your order")
    elif flag == 1:
        print("Order not available")
        if food_price > 100:
         food_price_with_discount = food_price*0.2
         food_price = food_price-food_price_with_discount
         print("Congratulations you got 20 percent discount on Order paid only:", food_price, "rs")
    else:
       print("Sorry No Discount")
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()

    file1.seek(0)
    file1.truncate()
    json.dump(content1, file1, indent=4)
    file1.close()


def update_user_profile(user_json, user_id, name, password, age, email, phn, address):
    flag = 0
    file = open(user_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == user_id:
            flag = 1
            content[i]["name"] = name
            content[i]["password"] = password
            content[i]["age"] = age
            content[i]["email"] = email
            content[i]["phone_number"] = phn
            content[i]["address"] = address
            print("updation Successfull")
    if flag == 0:
        print("Enter valid User Id")

    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()


def add_food(food_json, food_name, no_plates=1):
    food = {
        "id": 1,
        "name": food_name,
        "no of plates": no_plates
    }
    try:
        fp = open(food_json, "r+")
        content = json.load(fp)
        for i in range(len(content)):
            if content[i]["name"] == food_name:
                fp.close()
                return "Food Already Available"
        food["id"] = len(content)+1
        content.append(food)
    except json.JSONDecodeError:
        content = []
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content, fp, indent=4)
    fp.close()
    return "Success"


def update_food(food_json, food_id, no_plates=1):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no of plates"] += no_plates
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"


def remove_food(food_json, food_id):
    file = open(food_json, "r+")
    content = json.load(file)
    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent=4)
            file.close()
            return "success"
    return "Pls Enter Valid ID"


def read_food(food_json):
    file = open(food_json)
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print("Id: ", content[i]["id"])
        print(f"---> Name: {content[i]['name']}")
        print(f"---> Number of Plates: {content[i]['no of plates']}")
    file.close()
    return True


val = input("Do you Want to order Food Y/n: ")
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = input("Choose one value from the above: ")
    if val1 == "1":
        #--------------Register----------------#
        print()
        name = input("Enter the name: ")
        password = input("Enter the password: ")
        age = int(input("Enter your Age"))
        phn = input("Enter the Phn number")
        register_user("user.json", name, password, age, phn)

    elif val1 == "2":
        #--------------Login-------------------#
        print()
        while True:
            print("1) User")
            print("2) Admin")
            print("3) Exit")
            val2 = input("Choose on value from above: ")
            if val2 == "1":
                print("---------USER--------")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("user.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3 = input("Enter your Choice User!! ")
                                if val3 == "1":
                                    read_food("food.json")
                                elif val3 == "2":
                                    user_id = input("Enter User Id:")
                                    food_name = input(
                                        "Enter the Food You want to Eat")
                                    quantity = int(
                                        input("Enter the quantity of food"))
                                    user_place_order ("user.json", "food.json", user_id, food_name, quantity)
                                elif val3 == "3":
                                    user_id = int(input("Enter UserID :"))
                                    user_order_history("user.json", user_id)
                                elif val3 == "4":
                                    user_id = int(input("Enter UserID :"))
                                    name = input("Enter the new User Name")
                                    password = input("Enter the new Password")
                                    age = input("Updated Age")
                                    phn = input("Enter the new phone number")
                                    address = input("enter the address")
                                    update_user_profile(
                                        "user.json", user_id, name, password, age, phn, address)
                                else:
                                    print(
                                        "Thanks For Your Visit (Because it was free and you don't have money)")
                                    break
                        else:
                            print("Wrong Password!!")
                else:
                     print("Wrong Username!!")

            elif val2 == "2":
                print("$--------Admin------$")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food")
                            print("5) Exit")
                            val3 = input("Enter Your Choice Admin!!")
                            if val3 == "1":
                                food_name = input("Enter Food Name: ")
                                no_plates = int(
                                    input("Enter the Stock Value: "))
                                add_food("food.json", food_name, no_plates)
                            elif val3 == "2":
                                food_id = input("Enter Food ID: ")
                                no_plates = int(
                                    input("Enter the Stock Value: "))
                                update_food("food.json", food_id, no_plates)
                            elif val3 == "3":
                                read_food("food.json")
                            elif val3 == "4":
                                food_id = int(input("Enter FOODid :"))
                                remove_food("food.json", food_id)
                            else:
                                file.close()
                                print("%%%%Bye Bye%%%%%")
                                break
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:
        #--------------Exit--------------------#
        print("Have A Good Day!!")
        break
