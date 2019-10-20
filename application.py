from utilities import text2binary
from line_coding_schemes import AMI
# from PIL import ImageTk
# import PIL.Image
from tkinter import *
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from line_coding_schemes import *
import utilities as utils
import matplotlib.pyplot as plt
from matplotlib import style
import sys
import math
style.use("ggplot")

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

app = Tk()
app.title("Line Coding Visualization")
app.geometry('1366x758')
app.configure(background='#888888')
app.wm_iconbitmap('LOGO.ico')

top_frame = Frame(app, bg = '#888888')
top_frame.pack(side = TOP)

bot_top_frame = Frame(top_frame, bg = '#888888')
bot_top_frame.pack(side = BOTTOM)

bottom_frame = Frame(app, bg = '#888888')
bottom_frame.pack(side = BOTTOM)

Label(top_frame, text='Text', bg = '#888888', fg = "White").pack()
e1 = Entry(top_frame, width = 50) 
e1.pack()

lbl = Label(top_frame, text="Output here", bg = '#888888', fg = "White")
lbl.pack()

def plot_on_canvas(message, func, code_type):
    coded_message = func(message)
    text_style = dict(fontsize=12, fontdict={'family': 'verdana'})
    if len(message) >= 10:
        text_style = dict(fontsize=100/len(message), fontdict={'family': 'verdana'})
    ax.clear()
    ax.text(0., 3., f"Binary: {utils.text2binary(message)}", **text_style)
    ax.set_title(code_type)
    plt.xticks(range(len(coded_message)+1))
    plt.yticks([-2,-1,0,1,2])
    plt.ylim((-math.log(len(coded_message)+1, 2),math.log(len(coded_message)+1, 2)))
    x_dat = []
    j=0
    for i in range(1, len(coded_message)+1):
        if code_type in ['Manchester', 'Diffrential Manchester', 'Polar RZ', '2B1Q']:
            try:
                ax.plot([j, j+0.5], [coded_message[i-1], coded_message[i-1]], color='g')
                if coded_message[i-1] != coded_message[i]:
                    ax.plot([j+0.5, j+0.5], [coded_message[i-1], coded_message[i]], color='g')
            except:
                ax.plot([j, j+0.5], [coded_message[i-1], coded_message[i-1]], color='g')
            j+=0.5
        else:
            try:
                ax.plot([j, j+1], [coded_message[i-1], coded_message[i-1]], color='g')
                if coded_message[i-1] != coded_message[i]:
                    ax.plot([j+1, j+1], [coded_message[i-1], coded_message[i]], color='g')
            except:
                ax.plot([j, j+1], [coded_message[i-1], coded_message[i-1]], color='g')
            j+=1
    canvas.get_tk_widget().pack(fill= BOTH, side = TOP)
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

x = Button(bot_top_frame, text='AMI',bg="#307867",fg = "yellow", command = ami, activebackground = "orange")
x.pack(side = LEFT)
# x.place(x=78,y=130,anchor = "center")

# pseudoternary button
def pseudoternary_t():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('Pseudoternary')
    # print(message)
    code_type = 'Pseudoternary'
    plot_on_canvas(message, pseudoternary, code_type)

x = Button(bot_top_frame, text='Pseudoternary',fg="#307867", command = pseudoternary_t, activebackground = "orange", bg = "yellow")
x.pack(side = LEFT)
# x.place(x=160,y=130,anchor = "center")


# NRZ_I button
def nrz_i():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('NRZ I')
    # print(message)
    code_type = 'NRZ I'
    plot_on_canvas(message, NRZ_I, code_type)

x = Button(bot_top_frame, text='NRZ I',fg="yellow", command = nrz_i, activebackground = "orange", bg = "#307867")
x.pack(side = LEFT)
# x.place(x=250,y=130,anchor = "center")



# NRZ_L button
def nrz_l():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('NRZ L')
    # print(message)
    code_type = 'NRZ L'
    plot_on_canvas(message, NRZ_L, code_type)

x = Button(bot_top_frame, text='NRZ L',fg="#307867", command = nrz_l, activebackground = "orange", bg = "yellow")
x.pack(side = LEFT)
# x.place(x=320,y=130,anchor = "center")



# polar_RZ button
def polar_rz():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('Polar RZ')
    # print(message)
    code_type = 'Polar RZ'
    plot_on_canvas(message, polarRZ, code_type)

x = Button(bot_top_frame, text='Polar RZ',fg="yellow", command = polar_rz, activebackground = "orange", bg = "#307867")
x.pack(side = LEFT)
# x.place(x=400,y=130,anchor = "center")

# twoBoneQ button
def twoB1Q():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('2B1Q')
    # print(message)
    code_type = '2B1Q'
    plot_on_canvas(message, twoBoneQ, code_type)

x = Button(bot_top_frame, text='2B1Q',fg="#307867", command = twoB1Q, activebackground = "orange", bg = "yellow")
x.pack(side = LEFT)
# x.place(x=475,y=130,anchor = "center")

# Manchester button
def manchester():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('Manchester')
    # print(message)
    code_type = 'Manchester'
    plot_on_canvas(message, Manchester, code_type)

x = Button(bot_top_frame, text='Manchester',fg="yellow", command = manchester, activebackground = "orange", bg = "#307867")
x.pack(side = LEFT)
# x.place(x=560,y=130,anchor = "center")


# diff_Manchester button
def diff_manchester():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('Diffrential Manchester')
    # print(message)
    code_type = 'Diffrential Manchester'
    plot_on_canvas(message, diff_Manchester, code_type)

x = Button(bot_top_frame, text='Diffrential Manchester',fg="#307867", command = diff_manchester, activebackground = "orange", bg = "yellow")
x.pack(side = LEFT)
# x.place(x=675,y=130,anchor = "center")


# MLT_3 button
def mlt_3():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('MLT 3')
    # print(message)
    code_type = 'MLT 3'
    plot_on_canvas(message, MLT_3, code_type)

x = Button(bot_top_frame, text='MLT 3',fg="yellow", command = mlt_3, activebackground = "orange", bg = "#307867")
x.pack(side = LEFT)
# x.place(x=775,y=130,anchor = "center")




# B8ZS button
def b8zS():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('B8ZS')
    # print(message)
    code_type = 'B8ZS'
    plot_on_canvas(message, B8ZS, code_type)

x = Button(bot_top_frame, text='B8ZS',fg="#307867", command = b8zS, activebackground = "orange", bg = "yellow")
x.pack(side = LEFT)
# x.place(x=848,y=130,anchor = "center")



# HDB_3 button
def hbd_3():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('HDB 3')
    # print(message)
    code_type = 'HDB 3'
    plot_on_canvas(message, HDB_3, code_type)

x = Button(bot_top_frame, text='HDB 3',fg="yellow", command = hbd_3, activebackground = "orange", bg = "#307867")
x.pack(side = LEFT)
# x.place(x=920,y=130,anchor = "center")


canvas = FigureCanvasTkAgg(fig, bottom_frame)
NavigationToolbar2Tk(canvas, app)
canvas.get_tk_widget().pack(side = TOP)

# bottom_frame.place(x=750,y=780,anchor = "center")

exit = Button(bottom_frame, text='Exit',fg="white",bg = "red" ,width=25, command=app.destroy)
exit.pack()

app.mainloop()