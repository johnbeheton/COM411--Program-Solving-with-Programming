import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax =plt.subplots()

def animate(frame):
    global ax
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    

def run():
  fig, ax = plt.subplots()
simple_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)
plt.show()
  
run()  