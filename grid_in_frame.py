from tkinter import*
master=Tk()

button1=Button(master,text="B1")
button1.grid(row=1,column=1)

button2=Button(master, text="B2")
button2.grid(row=1,column=3)

button3=Button(master,text="B3")
button3.grid(row=1,column=5)

button4=Button(master,text="B4")
button4.grid(row=1,column=7)

button5=Button(master,text="B5")
button5.grid(row=1,column=9)

master.mainloop()