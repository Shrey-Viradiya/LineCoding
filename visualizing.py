import line_coding.LineCoding_TirthHihoriya as lcth 
import utilities as utils
import line_coding.linecoding_shrey as lcs
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def plot_polar(file_path):
    with open(file_path, 'r') as file:
        message = file.read()
    coded_message = lcth.NRZ_L(message)
    ax.clear()
    ax.text(0, 1.2, f"{coded_message}: {len(coded_message)}")
    x_dat = []
    j=0
    for i in range(1, len(coded_message)):
        ax.plot([j, j+1], [coded_message[i-1], coded_message[i-1]], color='g')
        if coded_message[i-1] != coded_message[i]:
            ax.plot([j+1, j+1], [coded_message[i-1], coded_message[i]], color='g')
        j+=1

def animate(i):
    plot_polar('message.txt')

ani = FuncAnimation(fig, animate, interval=1000)
plt.show()