def login():
    while True:
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
        if usernameInput == "admin" and passwordInput == "1234":
            return True

def showMenu():
    print("----- iShop -----")
    print("1. Price Calculator")
    print("หมายเลขอื่นๆ Log out")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login()==True:
    showMenu()
    if menuSelect()==1 :
        print(priceCalculator())
    else:
        print("Log out!")