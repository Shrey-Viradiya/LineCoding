import LineCoding_TirthHihoriya as lcth 
import utilities as utils 
import linecoding_shrey as lcs 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def plot_polar(file_path):
    with open(file_path, 'r') as file:
        message = file.read()
    coded_message = lcth.NRZ_L(message)
    ax.clear()
    ax.text(0.5, 0.5, f"{coded_message}: {len(coded_message)}")
    x_dat = []
    j=0
    k=0
    for i in range(len(coded_message)):
        if k == 2:
            j = j + 1
            k=0
        x_dat.append(j)
        k+=1
    ax.plot(x_dat, coded_message, color='r')

def animate(i):
    plot_polar('message.txt')

ani = FuncAnimation(fig, animate, interval=1000)
plt.show()