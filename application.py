from utilities import text2binary
from line_coding_schemes import AMI
from PIL import ImageTk
import PIL.Image
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
    res= ''.join(str(x) for x in AMI(e1.get()))
    lbl.configure(text= res)
    ax1.set_title('AMI')    
    
    # panel.pack()

x = Button(bot_top_frame, text='AMI',fg="blue", command = ami)
x.pack()

# img = ImageTk.PhotoImage(PIL.Image.open("temp.jpg"))
# panel = Label(app, image = img)

figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, bot_top_frame)
bar1.get_tk_widget().pack(fill= BOTH)


bottom_frame = Frame(app, height = 400)
bottom_frame.pack(side = BOTTOM)







# exit
exit = Button(bottom_frame, text='Stop',fg="red" ,width=25, command=app.destroy)
exit.pack()



# top_space = Canvas(app, width=10, height=25) 
# top_space.grid(row = 0,column = 2)



# middle_space = Canvas(app, width=10, height=25)
# middle_space.grid(row = 2,column = 2) 






# #  



# bottom_space = Canvas(app, width=10, height=25)
# bottom_space.grid(row = 7,column = 0) 

app.mainloop()