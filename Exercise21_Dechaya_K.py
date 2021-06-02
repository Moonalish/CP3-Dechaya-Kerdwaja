'''
    โปรแกรมBmI
'''

from tkinter import *
import math

def calculateBmi(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    
    labelResult.configure(text=(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)))
    x=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if  x>30 :
        labelBody.configure(text='อ้วนมาก')
    elif x>25:
        labelBody.configure(text='อ้วน')
    elif x>23:
        labelBody.configure(text='น้ำหนักเกิน')
    elif x>18.6:
        labelBody.configure(text='น้ำหนักสมส่วน')
    else:
        labelBody.configure(text='ผอมเกินไป')



   
window=Tk()
window.title('BMI')
window.minsize(width=250,height=150)

labelHeight = Label(window,text='ส่วนสูง(cm)')
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(window)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(window,text='น้ำหนัก(Kg)')
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(window)
textBoxWeight.grid(row=1,column=1)

calculateButton=Button(window,text='คำนวณ',bg="gray")
calculateButton.bind('<Button-1>',calculateBmi)
calculateButton.grid(row=2,column=1)

labelResult=Label(window,text='ผลลัพธ์')
labelResult.grid(row=3,column=1)

labelBody=Label(window,text='')
labelBody.grid(row=4,column=1)

window.mainloop()