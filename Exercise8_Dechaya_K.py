'''
    
    
        โปรแกรมสำหรับเช็คสินค้าและคำนวณสินค้ารวมค่า VAT



'''
username = input("กรอกชื่อผู้ใช้: ")
password = input("กรอกรหัสผ่าน: ")

if username == "Admin" and password == "123": # Check User Password
    print("ต้องการเช็คสินค้าที่มีอยู่หรือคำนวณเงินให้ลูกค้า")
    print("1.เช็คสินค้า")
    print("2.Price&VAT")
    userSelectet=int(input("ท่านต้องการทำรายการ: "))
    if userSelectet == 1: #Selectet form line 10.
        print("----สินค้าที่เรามี----")
        print("1.Starwberry cake")
        print("2.Bluebery cake")
        print("3.Short cake")
        print("4.Cocktail cake")
        Selectet = input("ท่านต้องการคำนวณเงินต่อหรอไม่(y,n): ")
        if Selectet == "y" :  #If you want.
            print("ท่านต้องการเค้กแต่ละชนิดกี่ชื้น")   
            a1 = int(input("Starwberry cake: "))
            a2 = int(input(".Bluebery cake: "))
            a3 = int(input("Short cake: "))
            a4 = int(input("Cocktail cake: "))
            price = a1*300+a2*200+a3*150+a4*530
            print("ราคารวม: ",price)
            vat = price*7/100
            total = price+vat
            print("รวมVAT 7%: ",total,"Bath")
        elif Selectet == "n":# If no.
            print("Thank you for service.")
        else: #If Worng
            print("Alert")
    elif userSelectet == 2:
            print("ท่านต้องการเค้กแต่ละชนิดกี่ชื้น")   
            a1 = int(input("Starwberry cake: "))
            a2 = int(input(".Bluebery cake: "))
            a3 = int(input("Short cake: "))
            a4 = int(input("Cocktail cake: "))
            price = a1*300+a2*200+a3*150+a4*530
            print("ราคารวม: ",price)
            vat = price*7/100
            total = price+vat
            print("รวมVAT 7%: ",total,"Bath")
else:
    print("User or Pass Worng!!!")           
