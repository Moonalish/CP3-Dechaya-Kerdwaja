x=int(input("number1: "))
y=int(input("number2: "))
def addNumber(x,y):
    print(x,"+",y,"=",x+y)
    value(x,y)

def value(x,y): #  - * /
    print(x,"-",y,"=",x-y)
    print(x,"*",y,"=",x*y)
    print(x,"/",y,"=",x/y)

addNumber(x,y)