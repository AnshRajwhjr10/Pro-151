# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:49:41 2021

@author: Ansh Raj
"""
from tkinter import*

root=Tk()
root.title("Country Capital")
root.geometry("500x500")
root.configure(background = "Yellow")

label_month = Label(root)
label_profit = Label(root)

label_max_profit = Label(root)
label_min_profit = Label(root)

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000,56000,30000,140000,67000,80000,6000,65000,9900000,68000,59999,20000)

label_month["text"] = "Month : " + str(month)
label_profit["text"] = "Profit : " + str(profits)

def maxprofit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    label_max_proft["text"] = "The maximum profit of " + str(max_profit)+ " was recorded in the month of " +str(max_profit_month)
    
def minprofit():
        min_profit = min(profits)
        min_profit_index = profits.index(min_profit)
        min_profit_month = month[min_profit_index]
        label_min_proft["text"] = "The minimum profit of " + str(min_profit)+ " was recorded in the month of " +str(min_profit_month)
 
label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5, rely=0.3, anchor=CENTER)

btn_max = Button(root, text="Show Max profitable month", command=maxProfit, bg = "Royal blue", fg = "white")
btn_min = Button(root, text="Show Min profitable month", command=minProfit, bg = "Royal blue", fg = "white")

btn_max.place(relx= 0.5, rely=0.4, anchor=CENTER)

label_max.place(relx= 0.5, rely=0.5, anchor=CENTER)

btn_min.place(relx= 0.5, rely=0.6, anchor=CENTER)

label_min.place(relx= 0.5, rely=0.7, anchor=CENTER)

root.mainloop()