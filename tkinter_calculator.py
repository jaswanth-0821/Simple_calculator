from tkinter import *
from PIL import Image

root = Tk()
root.title("Simple Calculator")
root.iconbitmap("icon1.ico")
e = Entry(root, font=10, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=12)


def click(num):
    e.insert(len(e.get()), num)


def equal():
    x = e.get()
    e.delete(0, END)
    e.insert(0, eval(x))


def dele():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=30, pady=30, command=lambda: click(1)).grid(
    row=3, column=0)
button_2 = Button(root, text="2", padx=30, pady=30, command=lambda: click(2)).grid(
    row=3, column=1)
button_3 = Button(root, text="3", padx=30, pady=30, command=lambda: click(3)).grid(
    row=3, column=2)
button_4 = Button(root, text="4", padx=30, pady=30, command=lambda: click(4)).grid(
    row=2, column=0)
button_5 = Button(root, text="5", padx=30, pady=30, command=lambda: click(5)).grid(
    row=2, column=1)
button_6 = Button(root, text="6", padx=30, pady=30, command=lambda: click(6)).grid(
    row=2, column=2)
button_7 = Button(root, text="7", padx=30, pady=30, command=lambda: click(7)).grid(
    row=1, column=0)
button_8 = Button(root, text="8", padx=30, pady=30, command=lambda: click(8)).grid(
    row=1, column=1)
button_9 = Button(root, text="9", padx=30, pady=30, command=lambda: click(9)).grid(
    row=1, column=2)
button_0 = Button(root, text="0", padx=30, pady=30, command=lambda: click(0)).grid(
    row=4, column=1)
button_equal = Button(root, text="=", padx=30, pady=30, command=equal).grid(
    row=4, column=2)
button_dot = Button(root, text=".", padx=30, pady=30).grid(
    row=4, column=0)

button_add = Button(root, text="+", padx=30, pady=30,
                    command=lambda: click("+")).grid(row=1, column=3)
button_sub = Button(root, text="-", padx=30, pady=30,
                    command=lambda: click("-")).grid(row=1, column=4)
button_mult = Button(root, text="x", padx=30, pady=30,
                     command=lambda: click("*")).grid(row=2, column=3)
button_div = Button(root, text="/", padx=30, pady=30,
                    command=lambda: click("/")).grid(row=2, column=4)
button_11 = Button(root, text="(", padx=30, pady=30,
                   command=lambda: click("(")).grid(row=3, column=3)
button_12 = Button(root, text=")", padx=30, pady=30,
                   command=lambda: click(")")).grid(row=3, column=4)
button_cle = Button(root, text="Clear", padx=50, pady=30,
                    command=dele).grid(row=4, column=3, columnspan=2)


root.mainloop()
