number = int(input("Input number: "))
for x in range(number):
    for y in range(number-x):
        print(" ",end="")
        text ="*"*(2*x+1)
    print(text)