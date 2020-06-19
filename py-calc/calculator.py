from tkinter import *
from PIL import Image 
from PIL import ImageTk

expression = ""

def press (num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression=""
    except:
        equation.set("Invalid Equation")
        expression=""

def clear():
    global expression
    expression=""
    equation.set("")

if __name__ == "__main__":
    window = Tk()
    window.configure(background="white")
    window.title("Calculator")
    window.geometry("280x300")

    equation = StringVar()

    expression_filed = Entry(window,textvariable=equation,font=("Aerial",20),fg="black")
    expression_filed.grid(columnspan=10,ipady=10,ipadx=70)

    width = 50
    height = 50

    img1 = Image.open("one.png")
    img1 = img1.resize((width,height))
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button (window, image = oneImage, bg = "gray", command = lambda: press(1), height =height, width = width)
    button1.grid(column=0,row=2)

    img1 = Image.open("one.png")
    img1 = img1.resize((width,height))
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button (window, image = oneImage, bg = "gray", command = lambda: press(1), height =height, width = width)
    button1.grid(column=0,row=2)

    img1 = Image.open("one.png")
    img1 = img1.resize((width,height))
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button (window, image = oneImage, bg = "gray", command = lambda: press(1), height =height, width = width)
    button1.grid(column=0,row=2)



    window.mainloop()