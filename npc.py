import random
from fpdf import FPDF
import math
import tkinter as tk
import webbrowser
pdf = FPDF()

window = tk.Tk()
window.title("Choose the Class")








def button_add(number):
    if number == 12:
        window.destroy()
        import wizard
        wizard




#define buttons
button_1 =tk.Button(window, text = "Barbarian", padx=40, pady=20, command = lambda:button_add(1))
button_2 =tk.Button(window, text = "Bard", padx=40, pady=20, command = lambda:button_add(2))
button_3 =tk.Button(window, text = "Cleric", padx=40, pady=20, command = lambda:button_add(3))
button_4 =tk.Button(window, text = "Druid", padx=40, pady=20, command = lambda:button_add(4))
button_5 =tk.Button(window, text = "Fighter", padx=40, pady=20, command = lambda:button_add(5))
button_6 =tk.Button(window, text = "Monk", padx=40, pady=20, command = lambda:button_add(6))
button_7 =tk.Button(window, text = "Paladin", padx=40, pady=20, command = lambda:button_add(7))
button_8 =tk.Button(window, text = "Ranger", padx=40, pady=20, command = lambda:button_add(8))
button_9 =tk.Button(window, text = "Rogue", padx=40, pady=20, command = lambda:button_add(9))
button_10 =tk.Button(window, text = "Sorceror", padx=40, pady=20, command = lambda:button_add(10))
button_11=tk.Button(window, text = "Warlock", padx=40, pady=20, command = lambda:button_add(11))
button_12 =tk.Button(window, text = "Wizard", padx=40, pady=20, command = lambda:button_add(12))

# put the buttons on the screen


button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=0, column=3)
button_5.grid(row=1, column=0)
button_6.grid(row=1, column=1)
button_7.grid(row=1, column=2)
button_8.grid(row=1, column=3)
button_9.grid(row=2, column=0)
button_10.grid(row=2, column=1)
button_11.grid(row=2, column=2)
button_12.grid(row=2, column=3)



window.mainloop()
