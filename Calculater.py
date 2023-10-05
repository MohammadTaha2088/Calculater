from tkinter import *
import tkinter.messagebox

window = Tk()

# ========================= settings =========================

window.title('Calculater')
window.resizable(width=False, height=False)
window.geometry('400x200')
color = 'gray'
window.configure(bg=color)

# ========================= variables =========================

input1 = StringVar()
input2 = StringVar()
result = StringVar()

# ========================= functions =========================

def error(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Error', 'An error occurred')
    else:
        tkinter.messagebox.showerror('Error', 'You can not divide by 0')


def plus():
    try:
        value = float(input1.get()) + float(input2.get())
        result.set(value)
    except:
        error('error')


def minus():
    try:
        value = float(input1.get()) - float(input2.get())
        result.set(value)
    except:
        error('error')


def multiply():
    try:
        value = float(input1.get()) * float(input2.get())
        result.set(value)
    except:
        error('error')


def divide():
    if input2.get() == '0':
        error('0')
    else:
        try:
            value = float(input1.get()) / float(input2.get())
            result.set(value)
        except:
            error('error')


# ========================= frames =========================

topFirst = Frame(window, width=400, height=50, bg=color)
topFirst.pack(side=TOP)

topSecond = Frame(window, width=400, height=50, bg=color)
topSecond.pack(side=TOP)

topThird = Frame(window, width=400, height=50, bg=color)
topThird.pack(side=TOP)

topFourth = Frame(window, width=400, height=50, bg=color)
topFourth.pack(side=TOP)

# ========================= labels =========================

label1 = Label(topFirst, text='Input number 1 :', bg=color)
label1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(topSecond, text='Input number 2 :', bg=color)
label2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(topFourth, text='Result :', bg=color)
label3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(topFourth, width=20, textvariable=result)
label4.pack(padx=10, pady=10)

# ========================= entries =========================

entry1 = Entry(topFirst, textvariable=input1)
entry1.pack(pady=10)

entry2 = Entry(topSecond, textvariable=input2)
entry2.pack(pady=10)

# ========================= buttons =========================

btn1 = Button(topThird, text='+', width=10, command=lambda: plus())
btn1.pack(side=LEFT, padx=10, pady=10)

btn2 = Button(topThird, text='-', width=10, command=lambda: minus())
btn2.pack(side=LEFT, padx=10, pady=10)

btn3 = Button(topThird, text='*', width=10, command=lambda: multiply())
btn3.pack(side=LEFT, padx=10, pady=10)

btn4 = Button(topThird, text='/', width=10, command=lambda: divide())
btn4.pack(side=LEFT, padx=10, pady=10)

# ========================= end =========================
window.mainloop()

print("let's test")