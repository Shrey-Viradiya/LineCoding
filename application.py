from utilities import text2binary
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

app = Tk()
app.title("Line Coding Visualization")

app.geometry('750x500')

top_space = Canvas(app, width=10, height=25) 
top_space.grid(row = 0,column = 2)

Label(app, text='Text').grid(row=1) 
e1 = Entry(app, width = 50) 
e1.grid(row=1, column=1) 

middle_space = Canvas(app, width=10, height=25)
middle_space.grid(row = 2,column = 2) 

lbl = Label(app, text="Output here") 
lbl.grid(column=2, row=6)

def AMI(message):
    output = []
    change = 1
    for x in text2binary(message):
        if (x == '0'):
            output.append(0)
        else:
            output.append(change)
            if(change == 1):
                change = -1
            else:
                change = 1
    return output

def ami():
    res= ''.join(str(x) for x in AMI(e1.get()))
    lbl.configure(text= res)

x = Button(app, text='AMI',fg="blue", command = ami)
x.grid(row = 4,column =1)

exit = Button(app, text='Stop',fg="red" ,width=25, command=app.destroy)
exit.grid(row = 5)

bottom_space = Canvas(app, width=10, height=25)
bottom_space.grid(row = 4,column = 0) 

app.mainloop()