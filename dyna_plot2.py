import matplotlib.pyplot as plt
# generate axes object
ax = plt.axes()

# set limits
plt.xlim(0,10) 
plt.ylim(0,10)

for i in range(10):        
     # add something to axes    
     ax.scatter([i], [i]) 
     ax.plot([i], [i+1], 'rx')

     # draw the plot
     plt.draw() 
     plt.pause(0.01) #is necessary for the plot to update for some reason

     # start removing points if you don't want all shown
     if i>2:
         ax.lines[0].remove()
         ax.collections[0].remove() 