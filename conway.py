import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sys
try:
    WORLD_DIMENSION, ALIVE, DEAD = int(sys.argv[1]), 255, 0
except:
    print('You need to give the value of the world dimension\n\nEXAMPLE:\npython conway.py 100')

world = np.random.choice([ALIVE, DEAD], WORLD_DIMENSION*WORLD_DIMENSION, p=[0.2, 0.8]).reshape(WORLD_DIMENSION, WORLD_DIMENSION)

def update(generations):
    global world
    newWorld = world.copy()
    for j in range(WORLD_DIMENSION):
        for i in range(WORLD_DIMENSION):
            total = (np.sum(world[(i-1):(i+2),(j-1):(j+2)])-world[i,j])/255
            if world[i, j]  == ALIVE and ((total < 2) or (total > 3)):
                newWorld[i, j] = DEAD
            elif total == 3:
                newWorld[i, j] = ALIVE
    mat.set_data(newWorld)
    world = newWorld
    return [mat]
    
fig, ax = plt.subplots()
mat = ax.matshow(world)
ani = animation.FuncAnimation(fig, update, interval=200, save_count=100)
plt.show()
