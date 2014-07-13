import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin

class Environment:
    def __init__(self):
        self.decrease = 1 #1m per dt
        self.currentSpeed = 50

    def update(self, speed):
        '''
        speed in m/s
        '''
        speed -= self.decrease
        self.currentSpeed += speed

    def getCurrentSpeed(self):
        return self.currentSpeed

class BangBangController:
    def __init__(self, targetSpeed, fullSpeed):
        self.targetSpeed = targetSpeed
        self.fullSpeed = fullSpeed


    def getOutput(self, currentSpeed):
        if currentSpeed > self.targetSpeed:
            return -self.fullSpeed
        elif currentSpeed < self.targetSpeed:
            return self.fullSpeed
        else:
            return 0



def update_line(num, data, line):
    line.set_data(data[...,:num])
    return line,

fig1 = plt.figure()

data = np.ndarray([2, 500])
l, = plt.plot([], [], 'r-')
plt.xlim([0, 500])
plt.ylim([-5, 1000])

env = Environment()
con = BangBangController(31, 5)

for i in range(500):
    data[0,i] = i
    data[1,i] = env.getCurrentSpeed()
    env.update(con.getOutput(env.getCurrentSpeed()))

line_ani = animation.FuncAnimation(fig1, update_line, fargs=(data, l),
    interval=100, blit=True)

plt.show()