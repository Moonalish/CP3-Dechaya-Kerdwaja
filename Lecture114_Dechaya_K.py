from currency_converter import CurrencyConverter
from tkinter import *

c = CurrencyConverter()
total = 0

def selectCurrency(event):
    select_cart_label.configure(text="If You Select THB Cart You Don't Paid VAT.")

    usd_cart_button = Button(window,text='USD CART',font=40,bg='#616A6B')
    usd_cart_button.bind('<Button-1>',current_USD)
    usd_cart_button.grid(row=6,column=2)   

    jpy_cart_button = Button(window,text='JPY CART',font=40,bg='#616A6B')
    jpy_cart_button.bind('<Button-1>',current_JPY)
    jpy_cart_button.grid(row=7,column=2)

    thb_cart_button = Button(window,text='THB CART',font=40,bg='#616A6B')
    thb_cart_button.bind('<Button-1>',current_THB)
    thb_cart_button.grid(row=8,column=2)

def current_USD(event):
    select_cart_label.configure(text='You Select USD Cart!!')
    total = int(whey1_box_input.get())*1000+int(whey2_box_input.get())*1500+int(whey3_box_input.get())*1800
    
    current_usd = c.convert(total,'THB','USD') #ส่วนแปลงค่าไทย เป็น ดอลล่า
    vat_usd = current_usd+(current_usd*(10/100))
    float_usd = ('TOTAL:'),'%.2f' % vat_usd ,('Dollar')

    result_label.configure(text=float_usd)
    done_button = Button(window,text='DONE',width=30,font=40,bg='#616A6B')
    done_button.bind('<Button-1>',exit)
    done_button.grid(row=10,column=2)


def current_JPY(event):
    select_cart_label.configure(text='You Select JPY Cart!!')
    total = int(whey1_box_input.get())*1000+int(whey2_box_input.get())*1500+int(whey3_box_input.get())*1800
    
    current_jpy = c.convert(total,'THB','JPY') #ส่วนแปลงค่าไทย เป็น ญี่ปุ่น
    vat_jpy = current_jpy+(current_jpy*(8/100))
    float_jpy = ('TOTAL:'),'%.2f' % vat_jpy ,('Yen')

    result_label.configure(text=float_jpy)
    done_button = Button(window,text='DONE',width=30,font=40,bg='#616A6B')
    done_button.bind('<Button-1>',exit)
    done_button.grid(row=10,column=2)

def current_THB(event):
    select_cart_label.configure(text='You Select THB Cart!!')
    THB_total = int(whey1_box_input.get())*1000+int(whey2_box_input.get())*1500+int(whey3_box_input.get())*1800,'BATH'

    
    result_label.configure(text=THB_total)
    done_button = Button(window,text='DONE',width=30,font=40,bg='#616A6B')
    done_button.bind('<Button-1>',exit)
    done_button.grid(row=10,column=2)


window = Tk()
window.title("Muscle Whey")
window.minsize(700,450)
window.configure(bg='#FCF3CF')

title_label = Label(window,text=" Welcome to Muscle Protien Shop"
,fg='Green',font=("Helvetica",16),anchor=W)
title_label.grid(row=0,column=2)

whey1_label = Label(window,text="Siam Protien(1000B./Pack)",bg='#FCF3CF',font=20)
whey1_label.grid(row=1,column=1)
whey1_box_input = Entry(window,width=23,font=14)
whey1_box_input.grid(row=1,column=2)

whey2_label = Label(window,text="Nice Guy Protein(1500B./Pack)",bg='#FCF3CF',font=20)
whey2_label.grid(row=2,column=1)
whey2_box_input = Entry(window,width=23,font=14)
whey2_box_input.grid(row=2,column=2)

whey3_label = Label(window,text="Samurai Protein(1800B./Pack)",bg='#FCF3CF',font=20)
whey3_label.grid(row=3,column=1)
whey3_box_input = Entry(window,width=23,font=14)
whey3_box_input.grid(row=3,column=2)

add_card = Button(window,text='Addcard',font=40,bg='#616A6B')
add_card.bind('<Button-1>',selectCurrency)
add_card.grid(row=4,column=2)

select_cart_label=Label(window,text="",bg='#FCF3CF',font=20)
select_cart_label.grid(row=5,column=2)

result_label=Label(window,text="",bg='#FCF3CF',font=20)
result_label.grid(row=9,column=2)

window.mainloop()
