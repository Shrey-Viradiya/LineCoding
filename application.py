from utilities import text2binary
from line_coding_schemes import AMI
# from PIL import ImageTk
# import PIL.Image
from tkinter import *
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from line_coding_schemes import *
import utilities as utils
import matplotlib.pyplot as plt
from matplotlib import style
import sys
import math
style.use("fast")

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
app = Tk()
app.title("Line Coding Visualization")
app.geometry('1366x700')

top_frame = Frame(app)
top_frame.pack()

Label(top_frame, text='Text').pack()
e1 = Entry(top_frame, width = 50) 
e1.pack() 

#bot_top_frame
bot_top_frame = Frame(top_frame)
bot_top_frame.pack(side = BOTTOM)

lbl = Label(bot_top_frame, text="Output here") 
lbl.pack()

def plot_on_canvas(message, func, code_type):
    coded_message = func(message)
    ax.clear()
    ax.text(0.1, 1.3, f"message: {message}, coded: {utils.text2binary(message)}, Coding to {code_type}")
    ax.set_title(code_type)
    plt.xticks(range(len(coded_message)+1))
    plt.yticks([-2,-1,0,1,2])
    plt.ylim((-math.log(len(coded_message)+1, 2),math.log(len(coded_message)+1, 2)))
    plt.grid()
    x_dat = []
    j=0
    for i in range(1, len(coded_message)+1):
        try:
            ax.plot([j, j+1], [coded_message[i-1], coded_message[i-1]], color='g')
            if coded_message[i-1] != coded_message[i]:
                ax.plot([j+1, j+1], [coded_message[i-1], coded_message[i]], color='g')
        except:
            ax.plot([j, j+1], [coded_message[i-1], coded_message[i-1]], color='g')
        j+=1
    canvas.get_tk_widget().pack(fill= BOTH)
    canvas.draw()

# AMI button
def ami():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('AMI')
    # print(message)
    code_type = 'AMI'
    plot_on_canvas(message, AMI, code_type)

x = Button(bot_top_frame, text='AMI',fg="blue", command = ami, activebackground = "orange", bg = "yellow")
x.pack(side = "left")

# pseudoternary button
def pseudoternary_t():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('pseudoternary')
    # print(message)
    code_type = 'pseudoternary'
    plot_on_canvas(message, pseudoternary, code_type)

x = Button(bot_top_frame, text='pseudoternary',fg="blue", command = pseudoternary_t, activebackground = "orange", bg = "yellow")
x.pack(side = "left")


# NRZ_I button
def nrz_i():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('NRZ_I')
    # print(message)
    code_type = 'NRZ_I'
    plot_on_canvas(message, NRZ_I, code_type)

x = Button(bot_top_frame, text='NRZ_I',fg="blue", command = nrz_i, activebackground = "orange", bg = "yellow")
x.pack(side = "left")


# NRZ_L button
def nrz_l():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('NRZ_L')
    # print(message)
    code_type = 'NRZ_L'
    plot_on_canvas(message, NRZ_L, code_type)

x = Button(bot_top_frame, text='NRZ_L',fg="blue", command = nrz_l, activebackground = "orange", bg = "yellow")
x.pack(side = "left")



# polar_RZ button
def polar_rz():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('polarRZ')
    # print(message)
    code_type = 'polarRZ'
    plot_on_canvas(message, polarRZ, code_type)

x = Button(bot_top_frame, text='polarRZ',fg="blue", command = polar_rz, activebackground = "orange", bg = "yellow")
x.pack(side = "left")

# twoBoneQ button
def twoB1Q():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('twoBoneQ')
    # print(message)
    code_type = 'twoBoneQ'
    plot_on_canvas(message, twoBoneQ, code_type)

x = Button(bot_top_frame, text='2B1Q',fg="blue", command = twoB1Q, activebackground = "orange", bg = "yellow")
x.pack(side = "left")

# Manchester button
def manchester():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('Manchester')
    # print(message)
    code_type = 'Manchester'
    plot_on_canvas(message, Manchester, code_type)

x = Button(bot_top_frame, text='Manchester',fg="blue", command = manchester, activebackground = "orange", bg = "yellow")
x.pack(side = "left")


# diff_Manchester button
def diff_manchester():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('diff_Manchester')
    # print(message)
    code_type = 'diff_Manchester'
    plot_on_canvas(message, diff_Manchester, code_type)

x = Button(bot_top_frame, text='diff_Manchester',fg="blue", command = diff_manchester, activebackground = "orange", bg = "yellow")
x.pack(side = "left")



# MLT_3 button
def mlt_3():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('MLT_3')
    # print(message)
    code_type = 'MLT_3'
    plot_on_canvas(message, MLT_3, code_type)

x = Button(bot_top_frame, text='MLT_3',fg="blue", command = mlt_3, activebackground = "orange", bg = "yellow")
x.pack(side = "left")



# B8ZS button
def b8zS():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('B8ZS')
    # print(message)
    code_type = 'B8ZS'
    plot_on_canvas(message, B8ZS, code_type)

x = Button(bot_top_frame, text='B8ZS',fg="blue", command = b8zS, activebackground = "orange", bg = "yellow")
x.pack(side = "left")


# HDB_3 button
def hbd_3():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('HDB_3')
    # print(message)
    code_type = 'HDB_3'
    plot_on_canvas(message, HDB_3, code_type)

x = Button(bot_top_frame, text='HDB_3',fg="blue", command = hbd_3, activebackground = "orange", bg = "yellow")
x.pack(side = "left")


canvas = FigureCanvasTkAgg(fig, bot_top_frame)
canvas.get_tk_widget().pack(fill= BOTH)

bottom_frame = Frame(app, height = 400)
bottom_frame.pack(side = "bottom")

exit = Button(bottom_frame, text='Stop',fg="red" ,width=25, command=app.destroy)
exit.pack()
app.mainloop()