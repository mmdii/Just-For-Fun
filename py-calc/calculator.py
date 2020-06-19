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
    window.geometry("320x300")

    equation = StringVar()

    expression_filed = Entry(window,textvariable=equation,font=("Aerial",20),fg="black")
    expression_filed.grid(columnspan=10,ipady=10,ipadx=70)

    width = 50
    height = 50

    img1 = Image.open("calc/one.png")
    img1 = img1.resize((width,height))
    oneImage = ImageTk.PhotoImage(img1)
    button1 = Button (window, image = oneImage, bg = "gray", command = lambda: press(1), height =height, width = width)
    button1.grid(column=0,row=2)

    img2 = Image.open("calc/two.png")
    img2 = img2.resize((width,height))
    twoImage = ImageTk.PhotoImage(img2)
    button2 = Button (window, image = twoImage, bg = "gray", command = lambda: press(2), height =height, width = width)
    button2.grid(column=1,row=2)

    img3 = Image.open("calc/three.png")
    img3 = img3.resize((width,height))
    threeImage = ImageTk.PhotoImage(img3)
    button3 = Button (window, image = threeImage, bg = "gray", command = lambda: press(3), height =height, width = width)
    button3.grid(column=2,row=2)

    img4 = Image.open("calc/four.png")
    img4 = img4.resize((width,height))
    fourImage = ImageTk.PhotoImage(img4)
    button4 = Button (window, image = fourImage, bg = "gray", command = lambda: press(4), height =height, width = width)
    button4.grid(column=0,row=3)

    img5 = Image.open("calc/five.png")
    img5 = img5.resize((width,height))
    fiveImage = ImageTk.PhotoImage(img5)
    button5 = Button (window, image = twoImage, bg = "gray", command = lambda: press(5), height =height, width = width)
    button5.grid(column=1,row=3)

    img6 = Image.open("calc/six.png")
    img6 = img6.resize((width,height))
    sixImage = ImageTk.PhotoImage(img6)
    button6 = Button (window, image = sixImage, bg = "gray", command = lambda: press(6), height =height, width = width)
    button6.grid(column=2,row=3)

    img7 = Image.open("calc/seven.png")
    img7 = img7.resize((width,height))
    sevenImage = ImageTk.PhotoImage(img7)
    button7 = Button (window, image = sevenImage, bg = "gray", command = lambda: press(7), height =height, width = width)
    button7.grid(column=0,row=4)

    img8 = Image.open("calc/eight.png")
    img8 = img8.resize((width,height))
    eightImage = ImageTk.PhotoImage(img8)
    button8 = Button (window, image = eightImage, bg = "gray", command = lambda: press(8), height =height, width = width)
    button8.grid(column=1,row=4)

    img9 = Image.open("calc/nine.png")
    img9 = img9.resize((width,height))
    nineImage = ImageTk.PhotoImage(img9)
    button9 = Button (window, image = nineImage, bg = "gray", command = lambda: press(9), height =height, width = width)
    button9.grid(column=2,row=4)

    img0 = Image.open("calc/zero.png")
    img0 = img0.resize((width,height))
    zeroImage = ImageTk.PhotoImage(img0)
    button0 = Button (window, image = zeroImage, bg = "white", command = lambda: press(0), height =height, width = width)
    button0.grid(column=1,row=5)


    imgPlus = Image.open("calc/plus.png")
    imgPlus = imgPlus.resize((width,height))
    plusImage = ImageTk.PhotoImage(imgPlus)
    buttonPlus = Button (window, image = plusImage, bg = "gray", command = lambda: press("+"), height =height, width = width)
    buttonPlus.grid(column=3,row=3)

    imgMul = Image.open("calc/multi.png")
    imgMul = imgMul.resize((width,height))
    multiImage = ImageTk.PhotoImage(imgMul)
    buttonMul = Button (window, image = multiImage, bg = "gray", command = lambda: press("*"), height =height, width = width)
    buttonMul.grid(column=3,row=2)

    imgEqual = Image.open("calc/equal.png")
    imgEqual = imgEqual.resize((width,height))
    equalImage = ImageTk.PhotoImage(imgEqual)
    buttonEqual = Button (window, image = equalImage, bg = "gray", command = equalpress, height =height, width = width)
    buttonEqual.grid(column=2,row=5)

    imgClear = Image.open("calc/clear.png")
    imgClear = imgClear.resize((width,height))
    clearImage = ImageTk.PhotoImage(imgClear)
    buttonClear = Button (window, image = clearImage, bg = "gray", command = clear, height =height, width = width)
    buttonClear.grid(column=0,row=5)


    imgDiv = Image.open("calc/div.png")
    imgDiv = imgDiv.resize((width,height))
    DivImage = ImageTk.PhotoImage(imgDiv)
    buttonDiv = Button (window, image = DivImage, bg = "gray", command = lambda: press("/"), height =height, width = width)
    buttonDiv.grid(column=3,row=5)

    imgMin = Image.open("calc/min.png")
    imgMin = imgMin.resize((width,height))
    MinImage = ImageTk.PhotoImage(imgMin)
    buttonMin = Button (window, image = MinImage, bg = "gray", command = lambda: press("-"), height =height, width = width)
    buttonMin.grid(column=3,row=4)

    window.mainloop()
