from line_coding_schemes import *
import utilities as utils
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def plot_polar(file_path):
    with open(file_path, 'r') as file:
        message = file.read()
    code_type = 'pseudoternary'
    coded_message = pseudoternary(message)
    ax.clear()
    ax.text(0, 1.2, f"message: {message}, coded: {utils.text2binary(message)}, Coding to {code_type}")
    plt.xticks(range(len(coded_message)))
    plt.yticks([-2,-1,0,1,2])
    plt.ylim((-2.2, 2.2))
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

def animate(i):
    plot_polar('message.txt')

ani = FuncAnimation(fig, animate, interval=1000)
plt.show()