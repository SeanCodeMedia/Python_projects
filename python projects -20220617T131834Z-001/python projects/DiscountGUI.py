
import Tkinter
from Tkinter import *

import tkMessageBox


window = Tkinter.Tk()
window.title ("Discount calculator")
width = window.winfo_screenwidth()
height = window.winfo_screenheight() 

window.geometry (str (width)+"x"+str(height))

centerX = width/2 
centerY = height/2 


screen_height = window.winfo_screenheight()

L1 = Label(window, text="#Days")
L1.pack( side = LEFT)
L1.place (x = centerX-400, y = centerY)

Dayenter = Entry (window)
Dayenter.insert(1,"1")
Dayenter.pack()
Dayenter.place(x = centerX-350, y = centerY)


Textprice = Label(window, text = "price $")
Textprice.pack()
Textprice.place (x = centerX-200, y = centerY )

priceEnter = Entry (window)
priceEnter.pack()
priceEnter.insert(1,"0")
priceEnter.place(x = centerX-150, y=centerY)

DiscountLable = Label (window, text = "Discount $")
DiscountLable.pack()
DiscountLable.place(x = centerX, y = centerY)

DiscountEntry = Entry(window)
DiscountEntry.pack()
DiscountEntry.insert(1,"0")
DiscountEntry.place(x = centerX+80, y = centerY)



GetDays = int(Dayenter.get())

print GetDays

price = priceEnter.get()

cost = None

discount = DiscountEntry.get() 


def rental_car_cost (days = 1): 
    
    if days >= 7: 
        
       discount = price*days
        
       cost = discount - 50
        
       print cost

       answer01 = "your answer is "+ str(cost)

       tkMessageBox.showinfo("Your Discount", answer01)

        
       return cost 
        
    elif days >= 3:
        
      discount = price*days 
      cost = discount - 20
      print cost 

      answer01 = "your answer is "+ str(cost)

      tkMessageBox.showinfo("Your Discount", answer01)

      return cost

    elif days < 3:
        cost = price*days 
        print cost

        answer01 = str(cost)

        tkMessageBox.showinfo("Your Discount", answer01)


    	return cost

#rental_car_cost() 

def Answer ():
	
	rental_car_cost(GetDays) 



submit = Tkinter.Button (text = "submit", command = Answer)
submit.pack(padx = 15, pady = 15 )
submit.place(x=centerX, y=centerY+200)


window.mainloop() # the end of GUI 

