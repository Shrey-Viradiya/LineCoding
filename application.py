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
style.use("seaborn-ticks")

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

bot_top_frame = Frame(top_frame)
bot_top_frame.pack(side = BOTTOM)

lbl = Label(bot_top_frame, text="Output here") 
lbl.pack()

# AMI button
def ami():
    message = e1.get()
    # res= ''.join(str(x) for x in message)
    lbl.configure(text=message)
    ax.set_title('AMI')
    # print(message)
    code_type = 'AMI'
    coded_message = AMI(message)
    ax.clear()
    ax.text(0.1, 1.3, f"message: {message}, coded: {utils.text2binary(message)}, Coding to {code_type}")
    ax.set_title('AMI')
    plt.xticks(range(len(coded_message)))
    plt.yticks([-2,-1,0,1,2])
    plt.ylim((-2.2,2.2))
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

x = Button(bot_top_frame, text='AMI',fg="blue", command = ami)
x.pack()

canvas = FigureCanvasTkAgg(fig, bot_top_frame)
canvas.get_tk_widget().pack(fill= BOTH)

bottom_frame = Frame(app, height = 400)
bottom_frame.pack(side = BOTTOM)

exit = Button(bottom_frame, text='Stop',fg="red" ,width=25, command=app.destroy)
exit.pack()
app.mainloop()