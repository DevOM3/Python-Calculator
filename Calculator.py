from tkinter import *


def click(event):
    global value, ans, b1
    ip = event.widget.cget("text")

    if ip == "=":
        # print(value.get().isdigit())
        if value.get().isdigit():
            int(value.get())
        else:
            try:
                op = eval(value.get())
                value.set(op)
                ans.update()
            except:
                value.set("ERROR")
                ans.update()
    elif ip == "AC":
        value.set("")
        ans.update()
    elif ip == "BKSP":
        value.set(value.get()[::-1])
        ans.delete(0, 1)
        value.set(value.get()[::-1])
        ans.update()
    elif ip == "ON":
        b1.destroy()
        value = StringVar()
        value.set("")
        ans = Entry(root, textvar=value, font="lucida 35 bold", border=3, relief=GROOVE, width=9, justify=RIGHT)
        ans.place(x=0, y=0)
        b2 = Button(text="OFF", font="lucida 15", pady=10, padx=2, activebackground="black", activeforeground="white")
        b2.place(x=2, y=65)
        b2.bind("<Button-1>", click)
        b2.bind("<Key>", click)
    elif ip == "OFF":
        ans.destroy()
        b0.destroy()
        b1 = Button(text="ON", font="lucida 15", pady=10, padx=7, activebackground="black", activeforeground="white")
        b1.place(x=2, y=65)
        b1.bind("<Button-1>", click)
        b1.bind("<Key>", click)
    else:
        value.set(value.get() + ip)
        ans.update()


root = Tk()
# root.wm_iconbitmap("calc.ico")
root.title("Calculator")
root.geometry("240x363")
root.minsize(240, 363)
root.maxsize(240, 363)

value = StringVar()
value.set("")
ans = Entry(root, textvar=value, font="lucida 35 bold", border=3, relief=GROOVE, width=9, justify=RIGHT)
ans.place(x=0, y=0)

b0 = Button(text="OFF", font="lucida 15", padx=2, pady=10, activebackground="black", activeforeground="white")
b0.place(x=2, y=65)
b0.bind("<Button-1>", click)
b = Button(text="%", font="lucida 21", padx=6, pady=2, activebackground="black", activeforeground="white")
b.place(x=62, y=65)
b.bind("<Button-1>", click)

b = Button(text="AC", font="lucida 15", padx=8, pady=10, activebackground="black", activeforeground="white")
b.place(x=122, y=65)
b.bind("<Button-1>", click)

b = Button(text="BKSP", font="lucida 11", pady=15, padx=2, activebackground="black", activeforeground="white")
b.place(x=182, y=65)
b.bind("<Button-1>", click)


b = Button(text="7", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=2, y=125)
b.bind("<Button-1>", click)
root.bind("<Key>", click)
b = Button(text="8", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=62, y=125)
b.bind("<Button-1>", click)

b = Button(text="9", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=122, y=125)
b.bind("<Button-1>", click)

b = Button(text="/", font="lucida 21", padx=13, pady=2, activebackground="black", activeforeground="white")
b.place(x=182, y=125)
b.bind("<Button-1>", click)


b = Button(text="4", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=2, y=185)
b.bind("<Button-1>", click)

b = Button(text="5", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=62, y=185)
b.bind("<Button-1>", click)

b = Button(text="6", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=122, y=185)
b.bind("<Button-1>", click)

b = Button(text="*", font="lucida 21", padx=12, pady=2, activebackground="black", activeforeground="white")
b.place(x=182, y=185)
b.bind("<Button-1>", click)


b = Button(text="1", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=2, y=245)
b.bind("<Button-1>", click)

b = Button(text="2", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=62, y=245)
b.bind("<Button-1>", click)

b = Button(text="3", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=122, y=245)
b.bind("<Button-1>", click)

b = Button(text="-", font="lucida 21", padx=13, pady=2, activebackground="black", activeforeground="white")
b.place(x=182, y=245)
b.bind("<Button-1>", click)


b = Button(text=".", font="lucida 21", padx=14, pady=2, activebackground="black", activeforeground="white")
b.place(x=2, y=305)
b.bind("<Button-1>", click)

b = Button(text="0", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=62, y=305)
b.bind("<Button-1>", click)

b = Button(text="+", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=122, y=305)
b.bind("<Button-1>", click)

b = Button(text="=", font="lucida 21", padx=10, pady=2, activebackground="black", activeforeground="white")
b.place(x=182, y=305)
b.bind("<Button-1>", click)

root.mainloop()
